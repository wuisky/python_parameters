from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import launch
import sys
# from launch.substitutions import PathJoinSubstitution, TextSubstitution


def generate_launch_description():
    my_parameter = LaunchConfiguration('my_parameter')
    my_parameter_launch_arg = DeclareLaunchArgument('my_parameter',
                                                    description='this is description',
                                                    default_value='oorigin_arg')
    ros_params = LaunchConfiguration('ros_params')
    ros_params_arg = DeclareLaunchArgument('ros_params',
                                           description='realpath of ros_params.yml ',
                                           default_value='/home/ubuntu/hogehoge.yml')

    my_base_ns = LaunchConfiguration('base_ns')
    my_base_ns_arg = DeclareLaunchArgument('base_ns',
                                           description='base tech namespace',
                                           default_value='')

    return LaunchDescription([
        my_parameter_launch_arg,
        ros_params_arg,
        my_base_ns_arg,
        Node(
            package='python_parameters',
            executable='minimal_param_node',
            name='custom_minimal_param_node',
            namespace='wu',
            output='screen',
            emulate_tty=True,
            # parameters=[
            #     {'my_parameter': 'kkkearth'}
            # ]
            parameters=[
                ros_params,
                {
                    'param1': 1,
                    'my_parameter': my_parameter,
                },
                # {'my_parameter':  TextSubstitution(text=my_parameter)}
                # {
                #     'my_parameter': my_parameter,
                # }
            ])
    ])


if __name__ == '__main__':
    ls = launch.LaunchService(argv=sys.argv[1:])
    ls.include_launch_description(generate_launch_description())
    ls.run()
