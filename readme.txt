IFCPythonSDK   	->IFC解析器
	yapc	->Schema映射器
Tortuga		->数据中心
IFCRelation	->IFC引用关系图打印


Run:
IFC Schema映射
	yapc下		python __init__.py
IFC解析
	IFCPythonSDK下	python __init__.py
数据中心：
	tortuga下	python manage.py runserver
引用关系图打印：
	IfcRelatioin下	python ifc.py <filename> [-o <filetype>]
