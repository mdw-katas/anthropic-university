UNI := ./bin/uni

.PHONY: test build status next clean

test:
	cd tools/uni && go mod tidy && gofmt -l . && go vet ./... && go test -race -cover ./...

build:
	cd tools/uni && go build -o ../../bin/uni .

status: build
	$(UNI) status

next: build
	$(UNI) next

clean:
	rm -rf bin
