"""Exploration: unittest.mock.Mock answers everything — which means a
careless test asserts nothing.

deploy() consults service.is_ready() before proceeding. Hand it a bare
Mock and predict what happens: does the "safety check" ever say no?

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-07
"""

from unittest.mock import Mock

PREDICT_DEPLOY_RESULT = None    # deploy(Mock()), e.g. "deployed" / "aborted"
PREDICT_MOCK_TRUTHY = None      # bool(Mock().anything.at.all())
PREDICT_TYPO_FAILURE = None     # type NAME raised by calling a TYPO'D method — or "no exception"


def deploy(service):
    """Refuses to deploy unless the service says it is ready."""
    if service.is_ready():
        return "deployed"
    return "aborted"


def typo_failure_name():
    """Mocks even answer methods that do not exist. Or do they object?"""
    service = Mock()
    try:
        service.is_raedy()  # note the typo
        return "no exception"
    except Exception as caught:
        return type(caught).__name__


if __name__ == "__main__":
    print(f"deploy(Mock()) -> {deploy(Mock())!r}")
    print(f"bool(Mock().anything.at.all()) -> {bool(Mock().anything.at.all())}")
    print(f"calling a typo'd method -> {typo_failure_name()}")
    # A Mock never says no. Prefer the dumbest double that can fail honestly.
