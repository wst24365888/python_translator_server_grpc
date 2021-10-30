compile_proto:
	python -m grpc_tools.protoc -I ./protos --python_out=./src --grpc_python_out=./src ./protos/translator.proto

install_reqs:
	pip install -r requirements.txt

run:
	python server.py