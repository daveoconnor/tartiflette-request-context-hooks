from unittest.mock import MagicMock

import pytest
from tartiflette_request_context_hooks import BaseRequestContextHooks
from tartiflette_request_context_hooks.base_request_context_hooks import \
    RequestDataNotStoredException, RequestNotSetException
from tests.sample_hooks import ConcreteWorkingRequestContextHooks,\
    ConcreteRequestContextHooksNoLabel, ConcreteRequestContextHooks


class TestBaseRequestContextHooks:
    def test_init_missing_label(self):
        with pytest.raises(TypeError):
            temp_hook = ConcreteRequestContextHooksNoLabel()

    def test_init(self):
        conc_hooks = ConcreteRequestContextHooks()
        assert conc_hooks.handler is None
        assert conc_hooks.request is None

    @pytest.mark.asyncio
    async def test_request_not_set_exception(self):
        temp_hook = ConcreteRequestContextHooks()
        with pytest.raises(RequestNotSetException):
            await temp_hook()

    def test__ns_label(self):
        conc_hooks = ConcreteWorkingRequestContextHooks()
        assert conc_hooks._ns_label == (
                BaseRequestContextHooks._lib_label + '-'
                + ConcreteWorkingRequestContextHooks.label
        )

    def test_properties_setters(self):
        conc_hooks = ConcreteRequestContextHooks()
        conc_hooks.handler = MagicMock()
        conc_hooks.request = MagicMock()
        # noinspection PyTypeHints
        assert isinstance(conc_hooks._handler, MagicMock)
        # noinspection PyTypeHints
        assert isinstance(conc_hooks._request, MagicMock)
        # noinspection PyTypeHints
        assert isinstance(conc_hooks.handler, MagicMock)
        # noinspection PyTypeHints
        assert isinstance(conc_hooks.request, MagicMock)

    def test_concrete_is_async_context_manager(self):
        conc_hooks = ConcreteRequestContextHooks()
        with pytest.raises(AttributeError):
            with conc_hooks:
                assert True

    @pytest.mark.asyncio
    async def test_concrete_is_async_context_manager(self):
        conc_hooks = ConcreteRequestContextHooks()
        conc_hooks.request = {}
        async with conc_hooks:
            pass

    def test_requires_aenter(self):
        with pytest.raises(TypeError):
            class NoAenter(BaseRequestContextHooks):
                async def __aexit__(self):
                    pass

            na = NoAenter()

    def test_requires_aexit(self):
        with pytest.raises(TypeError):
            class NoAexit(BaseRequestContextHooks):
                async def __aenter(self):
                    pass

            na = NoAexit()

    @pytest.mark.asyncio
    async def test__call__no_data_set(self):
        temp_hooks = ConcreteRequestContextHooks()
        temp_hooks.request = {'fake': 'data'}
        with pytest.raises(RequestDataNotStoredException):
            await temp_hooks()

    @pytest.mark.asyncio
    async def test__call__data_set(self):
        temp_hooks = ConcreteWorkingRequestContextHooks()
        temp_hooks.request = {}
        async with temp_hooks:
            pass
        assert await temp_hooks() == 'foo'
