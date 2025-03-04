# Используем официальный образ с поддержкой protoc
FROM debian:bullseye-slim

# Устанавливаем необходимые зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
  python3 python3-pip \
  golang \
  curl unzip git && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# Устанавливаем protobuf (protoc)
ARG PROTOC_VERSION=23.4
RUN curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION}-linux-x86_64.zip && \
  unzip protoc-${PROTOC_VERSION}-linux-x86_64.zip -d /usr/local && \
  rm protoc-${PROTOC_VERSION}-linux-x86_64.zip

# Устанавливаем grpcio-tools для Python
RUN pip3 install --no-cache-dir grpcio-tools

# Устанавливаем плагины для Go (в модульном режиме)
ENV GO111MODULE=on
RUN go get google.golang.org/protobuf/cmd/protoc-gen-go@v1.28.1 && \
  go get google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.2.0

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы в контейнер
COPY . .

# Устанавливаем GOPATH/bin в PATH
ENV PATH="/root/go/bin:$PATH"

# Команда для генерации файлов
CMD ["sh", "-c", "mkdir -p gen/go gen/python && \
  protoc -I proto proto/bot/bot.proto \
  --go_out=./gen/go --go_opt=paths=source_relative \
  --go-grpc_out=./gen/go --go-grpc_opt=paths=source_relative && \
  python3 -m grpc_tools.protoc -Iproto \
  --python_out=./gen/python \
  --grpc_python_out=./gen/python \
  proto/bot/bot.proto && touch gen/python/bot/__init__.py"]