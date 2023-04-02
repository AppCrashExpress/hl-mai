#ifndef HTTPPRODUCTWEBSERVER_H
#define HTTPPRODUCTWEBSERVER_H

#include "Poco/DateTimeFormat.h"
#include "Poco/DateTimeFormatter.h"
#include "Poco/Exception.h"
#include "Poco/Net/HTTPRequestHandler.h"
#include "Poco/Net/HTTPRequestHandlerFactory.h"
#include "Poco/Net/HTTPServer.h"
#include "Poco/Net/HTTPServerParams.h"
#include "Poco/Net/HTTPServerRequest.h"
#include "Poco/Net/HTTPServerResponse.h"
#include "Poco/Net/ServerSocket.h"
#include "Poco/ThreadPool.h"
#include "Poco/Timestamp.h"
#include "Poco/Util/HelpFormatter.h"
#include "Poco/Util/Option.h"
#include "Poco/Util/OptionSet.h"
#include "Poco/Util/ServerApplication.h"

using Poco::DateTimeFormat;
using Poco::DateTimeFormatter;
using Poco::ThreadPool;
using Poco::Timestamp;
using Poco::Net::HTTPRequestHandler;
using Poco::Net::HTTPRequestHandlerFactory;
using Poco::Net::HTTPServer;
using Poco::Net::HTTPServerParams;
using Poco::Net::HTTPServerRequest;
using Poco::Net::HTTPServerResponse;
using Poco::Net::ServerSocket;
using Poco::Util::Application;
using Poco::Util::HelpFormatter;
using Poco::Util::Option;
using Poco::Util::OptionCallback;
using Poco::Util::OptionSet;
using Poco::Util::ServerApplication;

#include "../database/product.h"
#include "http_request_factory.h"

class HTTPProductServer : public Poco::Util::ServerApplication {
 public:
  HTTPProductServer() : _helpRequested(false) {}

  ~HTTPProductServer() {}

 protected:
  void initialize(Application& self) {
    loadConfiguration();
    ServerApplication::initialize(self);
  }

  void uninitialize() { ServerApplication::uninitialize(); }

  int main([[maybe_unused]] const std::vector<std::string>& args) {
    if (!_helpRequested) {
      database::Product::init();
      ServerSocket svs(Poco::Net::SocketAddress("0.0.0.0", 8081));
      std::cout << "svs" << std::endl;
      HTTPServer srv(new HTTPRequestFactory(DateTimeFormat::SORTABLE_FORMAT),
                     svs, new HTTPServerParams);
      std::cout << "srv" << std::endl;
      srv.start();
      std::cout << "start" << std::endl;
      waitForTerminationRequest();
      std::cout << "termrequest" << std::endl;
      srv.stop();
      std::cout << "stop" << std::endl;
    }
    return Application::EXIT_OK;
  }

 private:
  bool _helpRequested;
};
#endif  // !HTTPPRODUCTWEBSERVER_H
