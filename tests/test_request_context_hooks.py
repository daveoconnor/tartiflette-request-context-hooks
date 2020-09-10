from unittest.mock import Mock
from tartiflette_request_context_hooks import RequestContextHooks
from .sample_hooks import ConcreteWorkingRequestContextHooks


class TestRequestContextHooks:
    def test_init(self):
        manager = ConcreteWorkingRequestContextHooks()
        mock_middleware = Mock()
        mock_middleware.get_hooks_service_middleware = Mock(return_value='foo')
        hook = RequestContextHooks(
            context_manager=manager,
            server_middleware=mock_middleware
        )
        assert hook.service is manager
        assert hook.middleware == 'foo'


