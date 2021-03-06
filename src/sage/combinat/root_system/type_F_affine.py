"""
Root system data for (untwisted) type F affine
"""
#*****************************************************************************
#       Copyright (C) 2008-2009 Daniel Bump
#       Copyright (C) 2008-2009 Justin Walker
#       Copyright (C) 2008-2009 Nicolas M. Thiery <nthiery at users.sf.net>,
#
#  Distributed under the terms of the GNU General Public License (GPL)
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from cartan_type import CartanType_standard_untwisted_affine
class CartanType(CartanType_standard_untwisted_affine):
    def __init__(self):
        """
        EXAMPLES::

            sage: ct = CartanType(['F',4,1])
            sage: ct
            ['F', 4, 1]
            sage: ct._repr_(compact = True)
            'F4~'

            sage: ct.is_irreducible()
            True
            sage: ct.is_finite()
            False
            sage: ct.is_affine()
            True
            sage: ct.is_untwisted_affine()
            True
            sage: ct.is_crystallographic()
            True
            sage: ct.is_simply_laced()
            False
            sage: ct.classical()
            ['F', 4]
            sage: ct.dual()
            ['F', 4, 1]^*
            sage: ct.dual().is_untwisted_affine()
            False

        TESTS::

            sage: TestSuite(ct).run()
        """
        CartanType_standard_untwisted_affine.__init__(self, "F", 4)

    def dynkin_diagram(self):
        """
        Returns the extended Dynkin diagram for affine type F.

        EXAMPLES::

            sage: f = CartanType(['F', 4, 1]).dynkin_diagram()
            sage: f
            O---O---O=>=O---O
            0   1   2   3   4
            F4~
            sage: sorted(f.edges())
            [(0, 1, 1), (1, 0, 1), (1, 2, 1), (2, 1, 1), (2, 3, 2), (3, 2, 1), (3, 4, 1), (4, 3, 1)]

        """
        from dynkin_diagram import DynkinDiagram_class
        g = DynkinDiagram_class(self)
        for i in range(1, 4):
            g.add_edge(i, i+1)
        g.set_edge_label(2,3,2)
        g.add_edge(0, 1)
        return g

    def _latex_dynkin_diagram(self, label=lambda x: x, node_dist=2, dual=False):
        r"""
        Return a latex representation of the Dynkin diagram.

        EXAMPLES::

            sage: print CartanType(['F',4,1])._latex_dynkin_diagram()
            \draw (0 cm,0) -- (2 cm,0);
            {
            \pgftransformxshift{2 cm}
            \draw (0 cm,0) -- (2 cm,0);
            \draw (2 cm, 0.1 cm) -- +(2 cm,0);
            \draw (2 cm, -0.1 cm) -- +(2 cm,0);
            \draw (4.0 cm,0) -- +(2 cm,0);
            \draw[shift={(3.2, 0)}, rotate=0] (135 : 0.45cm) -- (0,0) -- (-135 : 0.45cm);
            \draw[fill=white] (0 cm, 0) circle (.25cm) node[below=4pt]{$1$};
            \draw[fill=white] (2 cm, 0) circle (.25cm) node[below=4pt]{$2$};
            \draw[fill=white] (4 cm, 0) circle (.25cm) node[below=4pt]{$3$};
            \draw[fill=white] (6 cm, 0) circle (.25cm) node[below=4pt]{$4$};
            }
            \draw[fill=white] (0, 0) circle (.25cm) node[below=4pt]{$0$};
        """
        if self.global_options('mark_special_node') in ['latex', 'both']:
            special_fill = 'black'
        else:
            special_fill = 'white'
        ret = "\\draw (0 cm,0) -- (%s cm,0);\n"%node_dist
        ret += "{\n\\pgftransformxshift{%s cm}\n"%node_dist
        ret += self.classical()._latex_dynkin_diagram(label, node_dist, dual)
        ret += "\n}\n\\draw[fill=%s] (0, 0) circle (.25cm) node[below=4pt]{$%s$};"%(special_fill, label(0))
        return ret

    def ascii_art(self, label = lambda x: x):
        """
        Returns a ascii art representation of the extended Dynkin diagram

        EXAMPLES::

            sage: print CartanType(['F',4,1]).ascii_art(label = lambda x: x+2)
            O---O---O=>=O---O
            2   3   4   5   6
        """
        if self.global_options('mark_special_node') in ['printing', 'both']:
            special_str = self.global_options('special_node_str')
        else:
            special_str = 'O'
        return special_str + "---O---O=>=O---O\n%s   %s   %s   %s   %s"%tuple(label(i) for i in (0,1,2,3,4))

