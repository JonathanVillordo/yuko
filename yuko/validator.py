"""Validation stuff"""
import abc
import typing


class AbstractValidator:
    @abc.abstractmethod
    def process(self, key: str, value: typing.Any):
        """Abstract method for a validation class

            Args:
                key(str): A key in a json/dictionary which will
                be validated.
                value(Any): A value which will be validated.
        """
        pass

    @abc.abstractmethod
    def key_not_present(self, key):
        """Sets an error if a key doesn't present in a data object."""
        pass
