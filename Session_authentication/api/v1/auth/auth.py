#!/usr/bin/env python3
"""function"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """auth func"""
        if path is None or (excluded_paths is None or []):
            return True
        normalized_path = path if path.endswith('/') else path + '/'
        if normalized_path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """auto header"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """current user function"""
        return None

    def session_cookie(self, request=None):
        """session cookie function"""
        if request is None:
            return None

        cookie = getenv('SESSION_NAME')

        return request.cookies.get(cookie)
