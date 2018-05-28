class SliceCondition(object):
    '''
    The SliceCondition class contains the condition specifications
    '''

    def __init__(self, pColumn, pOperation, pLiteral):
        ''' 
        Constructor
        '''
        self.column = pColumn
        self.operation = pOperation
        self.literal = pLiteral