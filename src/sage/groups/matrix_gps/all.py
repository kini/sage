from sage.misc.lazy_import import lazy_import

lazy_import('sage.groups.matrix_gps.linear', 'GL')
lazy_import('sage.groups.matrix_gps.linear', 'SL')
lazy_import('sage.groups.matrix_gps.symplectic', 'Sp')
lazy_import('sage.groups.matrix_gps.unitary', 'SU')
lazy_import('sage.groups.matrix_gps.unitary', 'GU')
lazy_import('sage.groups.matrix_gps.orthogonal', 'GO')
lazy_import('sage.groups.matrix_gps.orthogonal', 'SO')
lazy_import('sage.groups.matrix_gps.finitely_generated', 'MatrixGroup')

#from matrix_group_element import is_MatrixGroupElement
#from matrix_group import MatrixGroup, is_MatrixGroup

import sage.groups.matrix_gps.pickling_overrides
