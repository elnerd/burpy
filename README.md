This is a python module implementing the burp interfaces with type hinting.
The purpose of this module, is to have type-hinting when developing jython/python Burp plugins.

To use this module, simply do `import * from burpy.loader` instead of `import X from burp`.

Caveats:

* Python do not support method with multiple signatures. For methods where this is a problem, an optional parameter
`hey_see_docstring` is added to the interface method - this indicate that you should read the documentation for this
method. In some cases, it was possible to cover multiple signatures using the same method.

* java.net.Byte type are signed! Does not convert very well to ints 

Todos:

* Java modules are not available in Python. Interfaces of the most common ones are added to this module to serve typing
hints.
  * add java.net.Byte interface with typing hints
  * add java.net.Map interface with typing hints
* finish IContextMenuInvocation

    
