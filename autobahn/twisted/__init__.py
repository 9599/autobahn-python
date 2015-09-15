###############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) Tavendo GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
###############################################################################


from __future__ import absolute_import

# WebSocket protocol support
from autobahn.twisted.websocket import \
    WebSocketServerProtocol, \
    WebSocketClientProtocol, \
    WebSocketServerFactory, \
    WebSocketClientFactory

# Twisted Web support
from autobahn.twisted.resource import WebSocketResource, WSGIRootResource

# Twisted specific utilities (these should really be in Twisted, but
# they aren't, and we use these in example code, so it must be part of
# the public API)
from autobahn.twisted.util import sleep
from autobahn.twisted.choosereactor import install_reactor


__all__ = (
    # WebSocket
    'WebSocketServerProtocol',
    'WebSocketClientProtocol',
    'WebSocketServerFactory',
    'WebSocketClientFactory',

    # Twisted Web
    'WebSocketResource',

    # this should really be in Twisted
    'WSGIRootResource',

    # this should really be in Twisted
    'sleep',
    'install_reactor'
)
