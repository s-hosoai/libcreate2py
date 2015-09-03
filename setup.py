from setuptools import setup, find_packages
PACKAGE	= 'create2'
NAME 	= 'libcreate2py'
DESCRIPTION = 'iRobot Create2 library for Raspberry Pi'
AUTHOR	= 's-hosoai'
AUTHOR_EMAIL = 'shintaro.hosoai@gmail.com'
URL		= 'https://github.com/s-hosoai/libcreate2py'
VERSION = __import__(PACKAGE).__version__

setup(  
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description='README.rst',
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        license='MIT',
        url=URL,
        packages=find_packages(exclude=['tests.*', 'tests']),
        include_package_data=True,
        zip_safe=True,
        install_requires=['pyserial'],
        keywords='irobot, create2, raspberry pi',
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
    )
