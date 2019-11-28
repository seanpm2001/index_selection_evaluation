import logging


class DatabaseConnector:
    def __init__(self, db_name, db_system, autocommit=False, columns=[]):
        """db_system 'postgres' or 'hana'
        """
        self.db_name = db_name
        self.db_system = db_system
        self.autocommit = autocommit
        self.columns = columns

        logging.debug('Database connector created: {}'.format(db_name))

    def exec_only(self, statement):
        self._cursor.execute(statement)

    def exec_fetch(self, statement, one=True):
        self._cursor.execute(statement)
        if one:
            return self._cursor.fetchone()
        return self._cursor.fetchall()

    #  def create_index(self, index):
    #      if self.db_system != 'postgres':
    #          raise NotImplementedError('only postgres')
    #      table_name = index.columns[0].table
    #      statement = (f'create index {index.index_idx()} '
    #                   f'on {table_name} ({index.joined_column_names()})')
    #      self.exec_only(statement)
    #      size = self.exec_fetch(f'select relpages from pg_class c '
    #                             f'where c.relname = \'{index.index_idx()}\'')
    #      size = size[0]
    #      index.estimated_size = size * 8 * 1024

    #  def drop_index(self, index):
    #      if self.db_system != 'postgres':
    #          raise NotImplementedError('only postgres')
    #      statement = f'drop index {index.index_idx()}'
    #      self.exec_only(statement)

    #  def commit(self):
    #      if self.db_system != 'postgres':
    #          raise NotImplementedError('only postgres')
    #      self._connection.commit()

    #  def close(self):
    #      self._connection.close()
    #      logging.debug('Database connector closed: {}'.format(self.db_name))
    #      del self

    #  def rollback(self):
    #      if self.db_system != 'postgres':
    #          raise NotImplementedError('only postgres')
    #      self._connection.rollback()

    #  def indexable_columns(self, query):
    #      indexable_columns = []
    #      plan = self.get_plan(query)
    #      for column in self.columns:
    #          if column.name in str(plan):
    #              indexable_columns.append(column)
    #      return indexable_columns
