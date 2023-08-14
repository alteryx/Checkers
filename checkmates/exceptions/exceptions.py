"""Exceptions used in DataChecks."""
from enum import Enum


class MissingComponentError(Exception):
    """An exception raised when a component is not found in all_components()."""

    pass


class ObjectiveNotFoundError(Exception):
    """Exception to raise when specified objective does not exist."""

    pass


class ObjectiveCreationError(Exception):
    """Exception when get_objective tries to instantiate an objective and required args are not provided."""


class DataCheckInitError(Exception):
    """Exception raised when a data check can't initialize with the parameters given."""


class ValidationErrorCode(Enum):
    """Enum identifying the type of error encountered in holdout validation."""

    INVALID_HOLDOUT_LENGTH = "invalid_holdout_length"
    """invalid_holdout_length"""
    INVALID_HOLDOUT_GAP_SEPARATION = "invalid_holdout_gap_separation"
    """invalid_holdout_gap_separation"""
