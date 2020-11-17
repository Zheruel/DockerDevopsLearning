sleep 5
if curl -d "test" service2:8080 | grep -q 'test'; then
  echo "Tests passed!"
  exit 0
else
  echo "Tests failed!"
  exit 1
fi