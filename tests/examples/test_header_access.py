import pytest
from unittest.mock import MagicMock, PropertyMock, Mock, patch
from tartiflette_request_context_hooks.middleware import aiohttp
from tartiflette_request_context_hooks.examples.header_access import HeaderAccessRequestContextHooks


class MockRequest(dict):
    headers = {'foo': 'bar'}


class TestHeaderAccessRequestContextHooks:
    def test_header_access_example_init(self):
        HeaderAccessRequestContextHooks()

    @pytest.mark.asyncio
    async def test_header_access_example_enter(self, monkeypatch):
        service = HeaderAccessRequestContextHooks()
        service.request = MockRequest()
        async with service:
            pass
        assert await service() == 'bar'

    # todo: add a test that request data can't be copied forward
