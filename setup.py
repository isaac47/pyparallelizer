from distutils.core import setup
setup(
  name = 'pyparallelizer',  
  packages = ['pyparallelizer'],  
  version = '0.1',  
  license='MIT', 
  description = 'TYPE YOUR DESCRIPTION HERE',   
  author = 'Isaac YIMGAINGE',            
  author_email = 'isaac.yimgaing@gmail.com',     
  url = 'https://github.com/isaac47/pyparallelizer',
  download_url = 'https://github.com/isaac47/pyparallelizer/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['PYTHON', 'DATAFRAME', 'MULTIPROCESSING'],   
  install_requires=[            
          'pandas',
          'numpy',
          'itertools',
          'multiprocessing',,
          'tqdm'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',     
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)

