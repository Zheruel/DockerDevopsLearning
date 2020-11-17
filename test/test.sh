sleep 5
if curl -d "test" service2:8080 | grep -q '098f6bcd4621d373cade4e832627b4f6'; then
  echo "Tests passed!"
  exit 0
else
  echo "Tests failed!"
  exit 1
fi