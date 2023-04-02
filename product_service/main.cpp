#include "http_product_server.h"

int main(int argc, char* argv[]) {
  HTTPProductServer app;
  std::cout << "fuck you main" << std::endl;
  return app.run(argc, argv);
}
