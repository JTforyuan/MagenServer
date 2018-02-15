from setuptools import setup

setup(
	name='MagentaServer',
	version='1.0',
	packages=['server','server.main_bp'],
	include_package_data = True,
	zip_safe=False,
	author='JiaTang',
	install_requires=[
		'Flask>=0.10'
	]
)