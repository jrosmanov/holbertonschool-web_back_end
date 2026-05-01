#!/usr/bin/env python3
"""This is the session auth module"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """This is the class for session auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """This is the method for creating session for user"""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_code = uuid4()
        self.user_id_by_session_id[str(session_code)] = user_id
        return str(session_code)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """This is the method for getting user id from session id"""
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """This is the method for getting current user from request"""
        from models.user import User
        coks = self.session_cookie(request)
        id = self.user_id_for_session_id(coks)
        return User.get(id)

    def destroy_session(self, request=None):
        """This is the method for destroying session for user"""
        sesscook = self.session_cookie(request)
        if (request is None or sesscook is None):
            return False

        user_id = self.user_id_for_session_id(sesscook)
        if not user_id:
            return False

        del self.user_id_by_session_id[sesscook]
        return True
