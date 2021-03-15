try:
    from burp import IBurpCollaboratorClientContext, IBurpCollaboratorInteraction, IBurpExtender
    from burp import IBurpExtenderCallbacks, IContextMenuFactory, IContextMenuInvocation
    from burp import ICookie, IExtensionHelpers, IExtensionStateListener, IHttpListener
    from burp import IHttpRequestResponse, IHttpRequestResponsePersisted, IHttpRequestResponseWithMarkers
    from burp import IHttpService, IInterceptedProxyMessage, IIntruderAttack, IIntruderPayloadGenerator
    from burp import IIntruderPayloadGeneratorFactory, IIntruderPayloadProcessor, IMenuItemHandler
    from burp import IMessageEditor, IMessageEditorController, IMessageEditorTab, IMessageEditorTabFactory
    from burp import IParameter, IProxyListener, IRequestInfo, IResponseInfo, IResponseKeywords
    from burp import IResponseVariations, IScanIssue, IScannerCheck, IScannerInsertionPoint
    from burp import IScannerInsertionPointProvider, IScannerListener, IScanQueueItem
    from burp import IScopeChangeListener, ISessionHandlingAction, ITab, ITempFile, ITextEditor
except ImportError:
    from burpy import *
