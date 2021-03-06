# Copyright 2016 Nidium Inc. All rights reserved.
# Use of this source code is governed by a MIT license
# that can be found in the LICENSE file.

{
    'variables' : {
        'libapenetwork_output_path': '<(DEPTH)/build/',

        # Hack to workaround two gyp issues : 
        # - Variables defined in command line are not relativized (at all)
        #   https://code.google.com/p/gyp/issues/detail?id=72
        #
        # - Variables named with a "%" at the end are not relativized
        #   https://code.google.com/p/gyp/issues/detail?id=444
        'variables': {
            'third_party%': 'third-party',
            'libapenetwork_output_third_party_path': '<(libapenetwork_output_path)/third-party/',
            'libapenetwork_tests_output_path': '<(libapenetwork_output_path)/tests/',
        },
        'third_party_path': '<(DEPTH)/<(third_party)',
        'libapenetwork_tests_output_path': '<(libapenetwork_tests_output_path)',
        'libapenetwork_output_third_party_path': '<(libapenetwork_output_third_party_path)',

        'target_os%': '<(OS)',
        'mac_deployment_target': '10.7',
        'mac_sdk_version%': '10.11',

        'asan%': 0,
        'profiler%': 0,
        'unit_test%': 0,
    },
}
