#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from py2neo import Graph,Node,Relationship,NodeMatcher

# 连接Neo4j数据库
graph = Graph(' http://localhost:7474/db/data/',username='neo4j',password='123456')

a = Node('Person',name='jiwawa')
graph.create(a)
b = Node('Person',name='jerry')
graph.create(b)

# 创建关系例子
r = Relationship(a,'KNOWS',b)
graph.create(r)

# 读取节点信息
node = pd.DataFrame(graph.run('MATCH (n:`Person`) RETURN n LIMIT 25'))
#print(node)

# 读取关系信息
relation = pd.DataFrame(graph.run('MATCH (n:`Person`)-[r]->(m:`Person`) return n,m,type(r)'))
print(relation)

# 删除所有节点
graph.run('MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r')