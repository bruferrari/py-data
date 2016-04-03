from decimal import Decimal

class Relationship:
    """Class that represents relationship between datatables

        This class has all the informations that identify a relationship
        between tables.

    """
    def __init__(self, name, _from, to, on):
        """Constructor

            Args:
                name: Name
                from: table where comes from
                to: table where goes to
                on: instance of column
        """
        self._name = name
        self._from = _from
        self._to - to
        self._on = on

class DataTable:
    """Represents a data table.

        This class represents a datatable of a public governmental organ. Must
        be able to validate inserted rows according with columns. Rows must be
        stored here.

        Attributes:
            name: Name of table
            columns: [List of columns]
            references: [List of tables that this table points to, like _fk]
            referenced: [List of tables that points to this table]
    """
    def __init__(self, name):
        """Constructor

            Args:
                name: Name
        """
        self._name = name
        self._columns = []
        self._references = []
        self._referenced = []
        self._data = []

    def add_column(self, name, kind, desc=''):
        col = Column(name, kind, desc)
        self._columns.append(col)
        return col

    def add_references(self, name, to, on):
        """Creates a reference for this table to another table

            Args:
                name: Name of relationship
                to: instance of pointed table
                on: instance of column that relationship exists
        """
        relationship = Relationship(name, to, on)
        self._references.append(relationship)

    def add_referenced(self, name, by, on):
        """Creates a reference for another table that points to that

            Args:
                name: Name of relationship
                by: table that points to that
                on: instance of column that relationship exists
        """
        relationship = Relationship(name, by, self, on);
        self._referenced.append(relationship)

class Column:
    """Represents a column

        This class represents a column of datatable.

        Attributes:
            name: Name of column
            kind: Kind of column
            desc: Description (string) of column
    """
    def __init__(self, name, kind, desc=''):
        """Constructor
            Args:
                name: Name
                kind: Kind
                desc: Description
        """
        self._name = name
        self._kind = kind
        self._desc = desc

    def _validate(clazz, kind, data):
        if kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        elif kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif kind == 'numeric':
            try:
                value = Decimal(data)
            except:
                return False
            return True

    validate = classmethod(_validate)

    def __str__(self):
        _str = 'Col: {} : {} {}'.format(self._name,
                                        self._kind,
                                        self._desc)
        return _str


    @property
    def name(self):
        return self._name

    @property
    def kind(self):
        return self._kind

    @property
    def desc(self):
        return self._desc

class PrimaryKey(Column):
    """Represents PK

        PrimaryKey class, children of Column class.
        This class represents a primary key for DataTable.

        Attributes:
            is_pk: (boolean) flag to tag key as primary key
    """
    def __init__(self, name, kind, desc=None):
        super().__init__(name, kind, desc=desc)
        self._is_pk = True

    def __str__(self):
        _str = 'Col: {} : {} {}'.format(self._name,
                                        self._kind,
                                        self._desc)
        return '{} - {}'.format('PK', _str)
