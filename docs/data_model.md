# The odML data model

Data exchange requires that annotations, metadata, are also
shared. In order to allow interoperability both a common
(meta) data model, the format in which the metadata are exchanged, and
a common terminology are required.

Here, we briefly describe the *odML* data model. It is based on
the idea of key-value pairs like ``temperature = 26°C``.

The model is as simple as possible while being flexible, allowing
interoperability, and being customizable. The model defines three
entities (Property, Section, Document) whose relations and
elements are shown in the figure below.

![odml_logo](images/erModel.png "odML data model")

Property and Section are the core entities. A Section contains
Properties and can further have subsection thus building a tree-like
structure. The model does not constrain the content, which offers the
flexibility essential for comprehensive annotation of neuroscience
data.
