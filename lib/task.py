from database import database as db

class Task:

    def showTask(self, **params):
        q = ''' SELECT * FROM task WHERE id = %s '''
        if 'id' not in params:
            return {'error': 'Parameter "id" is required'}
        return db.selectObject(q, (params['id'], ))

    def listCategories(self, **params):
        w = ''
        p = []
        if 'parent_id' in params:
            w += ' AND parent_id = %s '
            p.append(params['parent_id'])
        q = ''' SELECT * FROM task_categories WHERE 1 = 1 {} '''.format(w)
        return db.selectObjects(q, tuple(p)) 

    def listTasks(self, **params):
        w = ''
        p = []
        if 'category_id' in params:
            w += " AND category_id = %s "
            p.append(params['category_id'])
        q = ''' SELECT id, name, description FROM task WHERE 1 = 1 {} '''.format(w)
        return db.selectObjects(q, tuple(p))
    
    def createCategory(self, **params):
        q = ''' INSERT INTO task_categories (name, parent_id) VALUES(%s, %s) '''
        
        if 'name' not in params:
            return {'error': 'Parameter "name" is required'}
        if 'parent_id' not in params:
            params['parent_id'] = None
        return db.do(q , (params['name'], params['parent_id']))

    def createTask(self, **params):
        allowed_params = ['name', 'description', 'content', 'category_id']
        c = []
        p = []
        for k, v in params.items():
            if k in allowed_params:
                c.append(k)
                p.append(v)
        v = ', '.join(['%s']*len(c))
        c = ', '.join(c)
        q = ''' INSERT INTO task ({}) VALUES({}) '''.format(c, v)
        if 'name' not in params:
            return {'error': 'Parameter "name" is required'}
        if 'category_id' not in params:
            return {'error': 'Parameter "category_id" is required'} 
        return db.do(q, tuple(p))



task = Task()
