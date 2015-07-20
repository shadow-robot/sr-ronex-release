Accessing Module parameters [C++]
====================================

.. toctree::
   :maxdepth: 2
   :glob:
   :hidden:


The example demonstrates how to access RoNeX modules listed in the
parameter server. For each module, the parameter server stores
parameters such as its product\_id, product\_name, ronex\_id, path, and
serial. Note that we assume here that RoNeX consists of a Bridge (IN)
module, and one or multiple General I/O module(s), although all modules
will display similar attributes.

The code
--------

First change directories to your **sr\_ronex\_examples** package.

.. code-block:: bash

    roscd sr_ronex_examples

C++ file **sr\_ronex\_parse\_parameter\_server.cpp** is located inside
the **src** directory.

.. code-block:: cpp

    #include <string>
    #include <ros/ros.h>
    #include <ros/console.h>
    #include <boost/lexical_cast.hpp>

    #include "sr_ronex_utilities/sr_ronex_utilities.hpp"

    class SrRonexParseParamExample
    {
    public:
      SrRonexParseParamExample()
      {
	find_general_io_modules_();
      }

      ~SrRonexParseParamExample() {}

    private:

      void find_general_io_modules_(void)
      {
	ros::Rate loop_rate(10);
	std::string param;
	while ( ros::param::get("/ronex/devices/0/ronex_id", param ) == false )
	{
	  ROS_INFO_STREAM( "Waiting for General I/O module to be loaded properly.\n" );
	  loop_rate.sleep();
	}

	std::string empty_ronex_id("");
	int next_ronex_parameter_id = ronex::get_ronex_param_id(empty_ronex_id);

	for (int ronex_parameter_id = 0;
	     ronex_parameter_id < next_ronex_parameter_id;
	     ronex_parameter_id++)
	{

	  std::string product_id;
	  std::string product_id_key = ronex::get_ronex_devices_string( ronex_parameter_id, std::string("product_id") );
	  ros::param::get( product_id_key, product_id );

	  std::string product_name;
	  std::string product_name_key = ronex::get_ronex_devices_string( ronex_parameter_id, std::string("product_name") );
	  ros::param::get( product_name_key, product_name );

	  std::string path;
	  std::string path_key = ronex::get_ronex_devices_string( ronex_parameter_id, std::string("path") );
	  ros::param::get( path_key, path );

	  std::string ronex_id;
	  std::string ronex_id_key = ronex::get_ronex_devices_string( ronex_parameter_id, std::string("ronex_id") );
	  ros::param::get( ronex_id_key, ronex_id );

	  std::string serial;
	  std::string serial_key = ronex::get_ronex_devices_string( ronex_parameter_id, std::string("serial") );
	  ros::param::get( serial_key, serial );

	  ROS_INFO_STREAM( "*** General I/O module " << ronex_parameter_id << " ***" );
	  ROS_INFO_STREAM( "product_id   = " << product_id );
	  ROS_INFO_STREAM( "product_name = " << product_name );
	  ROS_INFO_STREAM( "ronex_id     = " << ronex_id );
	  ROS_INFO_STREAM( "path         = " << path );
	  ROS_INFO_STREAM( "serial       = " << serial );
	}
      }

      std::string to_string_(int d)
      {
	return boost::lexical_cast<std::string>(d);
      }
    };

    int main(int argc, char **argv)
    {

      ros::init(argc, argv, "sr_ronex_parse_parameter_server");
      ros::NodeHandle n;
      SrRonexParseParamExample example;

      return 0;
    }


The Code Explained
^^^^^^^^^^^^^^^^^^

.. code-block:: c++

    ros::init(argc, argv, "sr_ronex_parse_parameter_server");

Initialize ROS. This allows ROS to do name remapping through the command
line -- not important here. This is also where we specify the name of
our node. Node names must be unique in a running system. The name used
here must be a base name (i.e., it cannot have a / in it).

.. code-block:: c++

    ros::NodeHandle n;

Create a handle to this process' node. The first NodeHandle created will
actually do the initialization of the node, and the last one destructed
will cleanup any resources the node was using.

.. code-block:: c++

    ros::Rate loop_rate(10);
    std::string param;
    while (ros::param::get("/ronex/devices/0/ronex_id", param ) == false)
    {
      ROS_INFO( "Waiting for General I/O module to be loaded properly." );
      loop_rate.sleep();
    }

Loop until at least one General I/O module has been properly loaded.

.. code-block:: c++

    std::string empty_ronex_id("");
    int next_ronex_parameter_id = ronex::get_ronex_param_id(empty_ronex_id);

This C++ version is more complicated than the Python version, because
parameters are NOT stored in a dictionary as in Python.

Index ``ronex_parameter_id`` starts from 0. When an empty string is
given to ``ronex::get_ronex_param_id`` as the input argument, it returns
the next available ``ronex_parameter_id``.

.. code-block:: c++

    for (int ronex_parameter_id = 0; ronex_parameter_id <
         next_ronex_parameter_id; ronex_parameter_id++)
    {
      std::string product_id; std::string product_id_key = ronex::get_ronex_devices_string( ronex_parameter_id,
                                                                                            std::string("product_id") );
      ros::param::get( product_id_key, product_id );
      std::string product_name;
      std::string product_name_key = ronex::get_ronex_devices_string( ronex_parameter_id, std::string("product_name") );
      ros::param::get( product_name_key, product_name );

      std::string path;
      std::string path_key = ronex::get_ronex_devices_string( ronex_parameter_id, std::string("path") );
      ros::param::get( path_key, path );

      std::string ronex_id;
      std::string ronex_id_key = ronex::get_ronex_devices_string( ronex_parameter_id, std::string("ronex_id") );
      ros::param::get( ronex_id_key, ronex_id );

      std::string serial;
      std::string serial_key = ronex::get_ronex_devices_string( ronex_parameter_id, std::string("serial") );
      ros::param::get( serial_key, serial );

      ROS_INFO_STREAM( "*** General I/O module " << ronex_parameter_id << " ***" );
      ROS_INFO_STREAM( "product_id   = " << product_id );
      ROS_INFO_STREAM( "product_name = " << product_name );
      ROS_INFO_STREAM( "ronex_id     = " << ronex_id );
      ROS_INFO_STREAM( "path         = " << path );
      ROS_INFO_STREAM( "serial       = " << serial );
    }


We retrieve the values of all parameters (i.e., product_id, product_name, ronex_id, path, and serial) related to the General I/O module, and output the data to console.

Note that if ronex_id (its type is string) has not been set to an alias name, its value is equal to the value of serial. And serial is an integer that starts from 1.

Running the code
^^^^^^^^^^^^^^^^

Make sure that a roscore is up and running:

.. code-block:: bash

    roscore

If you're running this code from your own workspace, you'll first need to build it using Catkin, if you're not sure how to do this you can follow the instructions :doc:`here </General/Create-a-package-to-interact-with-RoNeX>`.

Next sure that a roscore and the RoNeX driver are running (see :doc:`Launching the RoNeX driver </General/Launching-the-RoNeX-driver>`).

Once this is done we can run our C++ program:

.. code-block:: bash

    rosrun sr_ronex_examples sr_ronex_parse_parameter_server

You will see something similar to:

::

    [INFO] [1380018712.243856548]: *** General I/O module 0 ***
    [INFO] [1380018712.243969375]: product_id = 33554433
    [INFO] [1380018712.244016969]: product_name = general_io
    [INFO] [1380018712.244051559]: ronex_id = 2
    [INFO] [1380018712.244087449]: path = /ronex/general_io/2
    [INFO] [1380018712.244124994]: serial = 2
