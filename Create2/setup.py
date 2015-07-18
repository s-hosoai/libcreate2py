from setuptools import setup, find_packages  
version = '0.1.0'

setup(  
        name='libcreate2py',
        version=version,
        description="iRobot Create2 library for Raspberry Pi", #
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: Education",
            "Natural Language :: Japanese",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python",
            "Topic :: Education",
            "Topic :: Software Development :: Embedded Systems",
            "Topic :: System :: Hardware :: Hardware Drivers",
            "License :: OSI Approved :: MIT License",
            ],
        keywords='irobot, create2, raspberry pi',
        author='s-hosoai',
        author_email='junkmiyu@gmail.com',
        url='https://github.com/s-hosoai/libcreate2py',
        license='MIT',
        packages=find_packages(exclude=['examples', 'tests']),
        include_package_data=True,
        zip_safe=True,
        long_description='README.rst',
        install_requires=['pyserial'],
    )
