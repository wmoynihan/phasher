from distutils.core import setup
setup(
  name = 'phasher',         
  packages = ['phasher'],   
  version = '0.1',      
  license='MIT',        
  description = 'quickly check file hashes of various formats in python',   
  author = 'wa moy',                   
  author_email = 'wmoynihan+gh@softwaresecured.com',      
  url = 'https://github.com/user/wmoynihan/phasher',   
  download_url = 'https://github.com/wmoynihan/phasher/archive/v_01.tar.gz',    
  keywords = ['hash', 'compare', 'integrity'],   
  install_requires=[           
          'hashlib'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
) 
