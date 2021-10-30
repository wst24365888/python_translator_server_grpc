compile_proto:
	python -m grpc_tools.protoc -I ./protos --python_out=./src --grpc_python_out=./src ./protos/translator.proto

run:
	python server.py