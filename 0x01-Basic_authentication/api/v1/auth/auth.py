#!/usr/bin/env python3
"""
Definition of class Auth
"""
from flask import request
from typing import (
    List,
    TypeVar
)


class Auth:
    """
    Manages the api authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required for the given path.

        Args:
            path (str): The path to check.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from the Flask request.

        Args:
            request: The Flask request object. Defaults to None.

        Returns:
            str: The authorization header or None if not found.
        """
        if request is None:
            None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user based on the Flask request.

        Args:
            request: The Flask request object. Defaults to None.

        Returns:
            TypeVar('User'): The current user or None.
        """
        return None

    def BasicAuth(Auth):
        pass
