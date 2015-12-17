{
  'targets': [
    {
      'target_name': '<(module_name)',
      'sources': [
        'src/binding.cc',
      ],
      "include_dirs" : [
        '<!(node -e "require(\'nan\')")'
      ],
      'dependencies': [
        'deps/mpg123/mpg123.gyp:output'
      ],
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }
  ]
}
