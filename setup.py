from distutils.core import setup
setup(
  name = 'uigame',         # How you named your package folder (MyLib)
  packages = ['uigame'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A library to easily add UI elements to pygame',   # Give a short description about your library
  author = 'Freddie Rayner',                   # Type in your name
  author_email = 'rayner.freddie@btinternet.com',      # Type in your E-Mail
  url = 'https://github.com/oof6969696969/uigame/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/oof6969696969/uigame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['pygame', 'user interface', 'UI'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pygame',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ],
)
