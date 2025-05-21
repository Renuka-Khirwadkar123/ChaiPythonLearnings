->install uv
pip install uv

->create project

uv init <projectname>
eg: uv init chaicode

->run uv project
uv run main.py

->add packages

uv add langchain

->uv build

create distribution or wrap the project in zip file

->uv
to get information about commands


-----------------------------------------------

->How to handle scripts using uv

->run script in uv
uv run chaiexample.py

->run with  dependency
uv run --with 'flask' chaiexample.py

->add dependency in scripts
uv  add --script chaiexample.py 'flask' 'requests'



