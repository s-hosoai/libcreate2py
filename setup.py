from setuptools import setup, find_packages  
PACKAGE	= 'create2'
NAME 	= 'libcreate2py'
DESCRIPTION = 'iRobot Create2 library for Raspberry Pi'
AUTHOR	= 'Shintaro Hosoai'
AUTHOR_EMAIL = 'shintaro.hosoai@gmail.com'
URL		= 'https://github.com/s-hosoai/libcreate2py'
VERSION = __import__(PACKAGE).__version__

setup(  
        name=Name,
        version=VERSION,
        description=DESCRIPTION,
        long_description='README.rst',
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        license='MIT',
        url=URL,
        packages=find_packages(exclude=['tests.*', 'tests']),
        package_data=find_package_data(PACKAGE, only_in_packages=False),
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Education',
            'Natural Language :: Japanese',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Topic :: Education',
            'Topic :: Software Development :: Embedded Systems',
            'Topic :: System :: Hardware :: Hardware Drivers',
            'License :: OSI Approved :: MIT License',
            ],
        keywords='irobot, create2, raspberry pi',
        author='s-hosoai',
        author_email='junkmiyu@gmail.com',
        url='https://github.com/s-hosoai/libcreate2py',
        license='MIT',
        packages=find_packages(exclude=['examples', 'tests']),
        include_package_data=True,
        zip_safe=True,
        install_requires=['pyserial'],
    )
