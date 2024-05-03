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
        if path is excluded_paths:
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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user based on the Flask request.

        Args:
            request: The Flask request object. Defaults to None.

        Returns:
            TypeVar('User'): The current user or None.
        """
        return None
