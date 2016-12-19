<?php
$data = array(
  'bundles' => array(
    'player' => (object) array(
      'type' => 'player',
      'name' => 'Player',
      'base' => 'node_content',
      'module' => 'node',
      'description' => '',
      'help' => '',
      'has_title' => '1',
      'title_label' => 'Player',
      'custom' => '1',
      'modified' => '1',
      'locked' => '0',
      'disabled' => '0',
      'orig_type' => 'player',
      'disabled_changed' => FALSE,
      'bc_entity_type' => 'node',
    ),
    'team' => (object) array(
      'type' => 'team',
      'name' => 'Team',
      'base' => 'node_content',
      'module' => 'node',
      'description' => '',
      'help' => '',
      'has_title' => '1',
      'title_label' => 'Team Name',
      'custom' => '1',
      'modified' => '1',
      'locked' => '0',
      'disabled' => '0',
      'orig_type' => 'team',
      'disabled_changed' => FALSE,
      'bc_entity_type' => 'node',
    ),
  ),
  'fields' => array(
    'body' => array(
      'entity_types' => array(
        0 => 'node',
      ),
      'field_permissions' => array(
        'type' => '0',
      ),
      'indexes' => array(
        'format' => array(
          0 => 'format',
        ),
      ),
      'settings' => array(),
      'translatable' => '0',
      'storage' => array(
        'type' => 'field_sql_storage',
        'settings' => array(),
        'module' => 'field_sql_storage',
        'active' => '1',
        'details' => array(
          'sql' => array(
            'FIELD_LOAD_CURRENT' => array(
              'field_data_body' => array(
                'value' => 'body_value',
                'summary' => 'body_summary',
                'format' => 'body_format',
              ),
            ),
            'FIELD_LOAD_REVISION' => array(
              'field_revision_body' => array(
                'value' => 'body_value',
                'summary' => 'body_summary',
                'format' => 'body_format',
              ),
            ),
          ),
        ),
      ),
      'foreign keys' => array(
        'format' => array(
          'table' => 'filter_format',
          'columns' => array(
            'format' => 'format',
          ),
        ),
      ),
      'field_name' => 'body',
      'type' => 'text_with_summary',
      'module' => 'text',
      'active' => '1',
      'locked' => '0',
      'cardinality' => '1',
      'deleted' => '0',
      'columns' => array(
        'value' => array(
          'type' => 'text',
          'size' => 'big',
          'not null' => FALSE,
        ),
        'summary' => array(
          'type' => 'text',
          'size' => 'big',
          'not null' => FALSE,
        ),
        'format' => array(
          'type' => 'varchar',
          'length' => 255,
          'not null' => FALSE,
        ),
      ),
      'bundles' => array(
        'node' => array(
          0 => 'page',
          1 => 'article',
          2 => 'caswebpage',
          3 => 'sysdemo_20161010150510',
          4 => 'sys_ruleslink_node',
          5 => 'sys_staticpage',
          6 => 'eref_pub_relforms',
          7 => 'player',
        ),
      ),
    ),
    'field_player_bats' => array(
      'translatable' => '0',
      'entity_types' => array(),
      'settings' => array(
        'allowed_values' => array(
          'L' => 'Left',
          'R' => 'Right',
        ),
        'allowed_values_function' => '',
        'profile2_private' => FALSE,
      ),
      'storage' => array(
        'type' => 'field_sql_storage',
        'settings' => array(),
        'module' => 'field_sql_storage',
        'active' => '1',
        'details' => array(
          'sql' => array(
            'FIELD_LOAD_CURRENT' => array(
              'field_data_field_player_bats' => array(
                'value' => 'field_player_bats_value',
              ),
            ),
            'FIELD_LOAD_REVISION' => array(
              'field_revision_field_player_bats' => array(
                'value' => 'field_player_bats_value',
              ),
            ),
          ),
        ),
      ),
      'foreign keys' => array(),
      'indexes' => array(
        'value' => array(
          0 => 'value',
        ),
      ),
      'field_permissions' => array(
        'type' => '0',
      ),
      'field_name' => 'field_player_bats',
      'type' => 'list_text',
      'module' => 'list',
      'active' => '1',
      'locked' => '0',
      'cardinality' => '1',
      'deleted' => '0',
      'columns' => array(
        'value' => array(
          'type' => 'varchar',
          'length' => 255,
          'not null' => FALSE,
        ),
      ),
      'bundles' => array(
        'node' => array(
          0 => 'player',
        ),
      ),
    ),
    'field_player_birthday' => array(
      'translatable' => '0',
      'entity_types' => array(),
      'settings' => array(
        'granularity' => array(
          'month' => 'month',
          'day' => 'day',
          'year' => 'year',
          'hour' => 0,
          'minute' => 0,
          'second' => 0,
        ),
        'tz_handling' => 'none',
        'timezone_db' => '',
        'cache_enabled' => 0,
        'cache_count' => '4',
        'profile2_private' => FALSE,
        'todate' => '',
      ),
      'storage' => array(
        'type' => 'field_sql_storage',
        'settings' => array(),
        'module' => 'field_sql_storage',
        'active' => '1',
        'details' => array(
          'sql' => array(
            'FIELD_LOAD_CURRENT' => array(
              'field_data_field_player_birthday' => array(
                'value' => 'field_player_birthday_value',
              ),
            ),
            'FIELD_LOAD_REVISION' => array(
              'field_revision_field_player_birthday' => array(
                'value' => 'field_player_birthday_value',
              ),
            ),
          ),
        ),
      ),
      'foreign keys' => array(),
      'indexes' => array(),
      'field_permissions' => array(
        'type' => '0',
      ),
      'field_name' => 'field_player_birthday',
      'type' => 'datetime',
      'module' => 'date',
      'active' => '1',
      'locked' => '0',
      'cardinality' => '1',
      'deleted' => '0',
      'columns' => array(
        'value' => array(
          'type' => 'datetime',
          'mysql_type' => 'datetime',
          'pgsql_type' => 'timestamp without time zone',
          'sqlite_type' => 'varchar',
          'sqlsrv_type' => 'smalldatetime',
          'not null' => FALSE,
          'sortable' => TRUE,
          'views' => TRUE,
        ),
      ),
      'bundles' => array(
        'node' => array(
          0 => 'player',
        ),
      ),
    ),
    'field_player_death' => array(
      'translatable' => '0',
      'entity_types' => array(),
      'settings' => array(
        'granularity' => array(
          'month' => 'month',
          'day' => 'day',
          'year' => 'year',
          'hour' => 0,
          'minute' => 0,
          'second' => 0,
        ),
        'tz_handling' => 'none',
        'timezone_db' => '',
        'cache_enabled' => 0,
        'cache_count' => '4',
        'profile2_private' => FALSE,
        'todate' => '',
      ),
      'storage' => array(
        'type' => 'field_sql_storage',
        'settings' => array(),
        'module' => 'field_sql_storage',
        'active' => '1',
        'details' => array(
          'sql' => array(
            'FIELD_LOAD_CURRENT' => array(
              'field_data_field_player_death' => array(
                'value' => 'field_player_death_value',
              ),
            ),
            'FIELD_LOAD_REVISION' => array(
              'field_revision_field_player_death' => array(
                'value' => 'field_player_death_value',
              ),
            ),
          ),
        ),
      ),
      'foreign keys' => array(),
      'indexes' => array(),
      'field_permissions' => array(
        'type' => '0',
      ),
      'field_name' => 'field_player_death',
      'type' => 'datetime',
      'module' => 'date',
      'active' => '1',
      'locked' => '0',
      'cardinality' => '1',
      'deleted' => '0',
      'columns' => array(
        'value' => array(
          'type' => 'datetime',
          'mysql_type' => 'datetime',
          'pgsql_type' => 'timestamp without time zone',
          'sqlite_type' => 'varchar',
          'sqlsrv_type' => 'smalldatetime',
          'not null' => FALSE,
          'sortable' => TRUE,
          'views' => TRUE,
        ),
      ),
      'bundles' => array(
        'node' => array(
          0 => 'player',
        ),
      ),
    ),
    'field_player_height' => array(
      'translatable' => '0',
      'entity_types' => array(),
      'settings' => array(
        'profile2_private' => FALSE,
      ),
      'storage' => array(
        'type' => 'field_sql_storage',
        'settings' => array(),
        'module' => 'field_sql_storage',
        'active' => '1',
        'details' => array(
          'sql' => array(
            'FIELD_LOAD_CURRENT' => array(
              'field_data_field_player_height' => array(
                'value' => 'field_player_height_value',
              ),
            ),
            'FIELD_LOAD_REVISION' => array(
              'field_revision_field_player_height' => array(
                'value' => 'field_player_height_value',
              ),
            ),
          ),
        ),
      ),
      'foreign keys' => array(),
      'indexes' => array(),
      'field_permissions' => array(
        'type' => '0',
      ),
      'field_name' => 'field_player_height',
      'type' => 'number_integer',
      'module' => 'number',
      'active' => '1',
      'locked' => '0',
      'cardinality' => '1',
      'deleted' => '0',
      'columns' => array(
        'value' => array(
          'type' => 'int',
          'not null' => FALSE,
        ),
      ),
      'bundles' => array(
        'node' => array(
          0 => 'player',
        ),
      ),
    ),
    'field_player_id' => array(
      'translatable' => '0',
      'entity_types' => array(),
      'settings' => array(
        'max_length' => '255',
        'profile2_private' => FALSE,
      ),
      'storage' => array(
        'type' => 'field_sql_storage',
        'settings' => array(),
        'module' => 'field_sql_storage',
        'active' => '1',
        'details' => array(
          'sql' => array(
            'FIELD_LOAD_CURRENT' => array(
              'field_data_field_player_id' => array(
                'value' => 'field_player_id_value',
                'format' => 'field_player_id_format',
              ),
            ),
            'FIELD_LOAD_REVISION' => array(
              'field_revision_field_player_id' => array(
                'value' => 'field_player_id_value',
                'format' => 'field_player_id_format',
              ),
            ),
          ),
        ),
      ),
      'foreign keys' => array(
        'format' => array(
          'table' => 'filter_format',
          'columns' => array(
            'format' => 'format',
          ),
        ),
      ),
      'indexes' => array(
        'format' => array(
          0 => 'format',
        ),
      ),
      'field_permissions' => array(
        'type' => '0',
      ),
      'field_name' => 'field_player_id',
      'type' => 'text',
      'module' => 'text',
      'active' => '1',
      'locked' => '0',
      'cardinality' => '1',
      'deleted' => '0',
      'columns' => array(
        'value' => array(
          'type' => 'varchar',
          'length' => '255',
          'not null' => FALSE,
        ),
        'format' => array(
          'type' => 'varchar',
          'length' => 255,
          'not null' => FALSE,
        ),
      ),
      'bundles' => array(
        'node' => array(
          0 => 'player',
        ),
      ),
    ),
    'field_player_nick_name' => array(
      'translatable' => '0',
      'entity_types' => array(),
      'settings' => array(
        'max_length' => '255',
        'profile2_private' => FALSE,
      ),
      'storage' => array(
        'type' => 'field_sql_storage',
        'settings' => array(),
        'module' => 'field_sql_storage',
        'active' => '1',
        'details' => array(
          'sql' => array(
            'FIELD_LOAD_CURRENT' => array(
              'field_data_field_player_nick_name' => array(
                'value' => 'field_player_nick_name_value',
                'format' => 'field_player_nick_name_format',
              ),
            ),
            'FIELD_LOAD_REVISION' => array(
              'field_revision_field_player_nick_name' => array(
                'value' => 'field_player_nick_name_value',
                'format' => 'field_player_nick_name_format',
              ),
            ),
          ),
        ),
      ),
      'foreign keys' => array(
        'format' => array(
          'table' => 'filter_format',
          'columns' => array(
            'format' => 'format',
          ),
        ),
      ),
      'indexes' => array(
        'format' => array(
          0 => 'format',
        ),
      ),
      'field_permissions' => array(
        'type' => '0',
      ),
      'field_name' => 'field_player_nick_name',
      'type' => 'text',
      'module' => 'text',
      'active' => '1',
      'locked' => '0',
      'cardinality' => '1',
      'deleted' => '0',
      'columns' => array(
        'value' => array(
          'type' => 'varchar',
          'length' => '255',
          'not null' => FALSE,
        ),
        'format' => array(
          'type' => 'varchar',
          'length' => 255,
          'not null' => FALSE,
        ),
      ),
      'bundles' => array(
        'node' => array(
          0 => 'player',
        ),
      ),
    ),
    'field_player_notes' => array(
      'translatable' => '0',
      'entity_types' => array(),
      'settings' => array(
        'profile2_private' => FALSE,
      ),
      'storage' => array(
        'type' => 'field_sql_storage',
        'settings' => array(),
        'module' => 'field_sql_storage',
        'active' => '1',
        'details' => array(
          'sql' => array(
            'FIELD_LOAD_CURRENT' => array(
              'field_data_field_player_notes' => array(
                'value' => 'field_player_notes_value',
                'format' => 'field_player_notes_format',
              ),
            ),
            'FIELD_LOAD_REVISION' => array(
              'field_revision_field_player_notes' => array(
                'value' => 'field_player_notes_value',
                'format' => 'field_player_notes_format',
              ),
            ),
          ),
        ),
      ),
      'foreign keys' => array(
        'format' => array(
          'table' => 'filter_format',
          'columns' => array(
            'format' => 'format',
          ),
        ),
      ),
      'indexes' => array(
        'format' => array(
          0 => 'format',
        ),
      ),
      'field_permissions' => array(
        'type' => '0',
      ),
      'field_name' => 'field_player_notes',
      'type' => 'text_long',
      'module' => 'text',
      'active' => '1',
      'locked' => '0',
      'cardinality' => '1',
      'deleted' => '0',
      'columns' => array(
        'value' => array(
          'type' => 'text',
          'size' => 'big',
          'not null' => FALSE,
        ),
        'format' => array(
          'type' => 'varchar',
          'length' => 255,
          'not null' => FALSE,
        ),
      ),
      'bundles' => array(
        'node' => array(
          0 => 'player',
        ),
      ),
    ),
    'field_player_throws' => array(
      'translatable' => '0',
      'entity_types' => array(),
      'settings' => array(
        'allowed_values' => array(
          'L' => 'Left',
          'R' => 'Right',
        ),
        'allowed_values_function' => '',
        'profile2_private' => FALSE,
      ),
      'storage' => array(
        'type' => 'field_sql_storage',
        'settings' => array(),
        'module' => 'field_sql_storage',
        'active' => '1',
        'details' => array(
          'sql' => array(
            'FIELD_LOAD_CURRENT' => array(
              'field_data_field_player_throws' => array(
                'value' => 'field_player_throws_value',
              ),
            ),
            'FIELD_LOAD_REVISION' => array(
              'field_revision_field_player_throws' => array(
                'value' => 'field_player_throws_value',
              ),
            ),
          ),
        ),
      ),
      'foreign keys' => array(),
      'indexes' => array(
        'value' => array(
          0 => 'value',
        ),
      ),
      'field_permissions' => array(
        'type' => '0',
      ),
      'field_name' => 'field_player_throws',
      'type' => 'list_text',
      'module' => 'list',
      'active' => '1',
      'locked' => '0',
      'cardinality' => '1',
      'deleted' => '0',
      'columns' => array(
        'value' => array(
          'type' => 'varchar',
          'length' => 255,
          'not null' => FALSE,
        ),
      ),
      'bundles' => array(
        'node' => array(
          0 => 'player',
        ),
      ),
    ),
    'field_player_weight' => array(
      'translatable' => '0',
      'entity_types' => array(),
      'settings' => array(
        'profile2_private' => FALSE,
      ),
      'storage' => array(
        'type' => 'field_sql_storage',
        'settings' => array(),
        'module' => 'field_sql_storage',
        'active' => '1',
        'details' => array(
          'sql' => array(
            'FIELD_LOAD_CURRENT' => array(
              'field_data_field_player_weight' => array(
                'value' => 'field_player_weight_value',
              ),
            ),
            'FIELD_LOAD_REVISION' => array(
              'field_revision_field_player_weight' => array(
                'value' => 'field_player_weight_value',
              ),
            ),
          ),
        ),
      ),
      'foreign keys' => array(),
      'indexes' => array(),
      'field_permissions' => array(
        'type' => '0',
      ),
      'field_name' => 'field_player_weight',
      'type' => 'number_integer',
      'module' => 'number',
      'active' => '1',
      'locked' => '0',
      'cardinality' => '1',
      'deleted' => '0',
      'columns' => array(
        'value' => array(
          'type' => 'int',
          'not null' => FALSE,
        ),
      ),
      'bundles' => array(
        'node' => array(
          0 => 'player',
        ),
      ),
    ),
    'field_team_park' => array(
      'translatable' => '0',
      'entity_types' => array(),
      'settings' => array(
        'max_length' => '255',
        'profile2_private' => FALSE,
      ),
      'storage' => array(
        'type' => 'field_sql_storage',
        'settings' => array(),
        'module' => 'field_sql_storage',
        'active' => '1',
        'details' => array(
          'sql' => array(
            'FIELD_LOAD_CURRENT' => array(
              'field_data_field_team_park' => array(
                'value' => 'field_team_park_value',
                'format' => 'field_team_park_format',
              ),
            ),
            'FIELD_LOAD_REVISION' => array(
              'field_revision_field_team_park' => array(
                'value' => 'field_team_park_value',
                'format' => 'field_team_park_format',
              ),
            ),
          ),
        ),
      ),
      'foreign keys' => array(
        'format' => array(
          'table' => 'filter_format',
          'columns' => array(
            'format' => 'format',
          ),
        ),
      ),
      'indexes' => array(
        'format' => array(
          0 => 'format',
        ),
      ),
      'field_permissions' => array(
        'type' => '0',
      ),
      'field_name' => 'field_team_park',
      'type' => 'text',
      'module' => 'text',
      'active' => '1',
      'locked' => '0',
      'cardinality' => '1',
      'deleted' => '0',
      'columns' => array(
        'value' => array(
          'type' => 'varchar',
          'length' => '255',
          'not null' => FALSE,
        ),
        'format' => array(
          'type' => 'varchar',
          'length' => 255,
          'not null' => FALSE,
        ),
      ),
      'bundles' => array(
        'node' => array(
          0 => 'team',
        ),
      ),
    ),
    'field_teams' => array(
      'translatable' => '0',
      'entity_types' => array(),
      'settings' => array(
        'profile2_private' => FALSE,
        'target_type' => 'node',
        'handler' => 'base',
        'handler_settings' => array(
          'target_bundles' => array(
            'team' => 'team',
          ),
          'sort' => array(
            'type' => 'none',
          ),
          'behaviors' => array(
            'views-select-list' => array(
              'status' => 0,
            ),
          ),
        ),
      ),
      'storage' => array(
        'type' => 'field_sql_storage',
        'settings' => array(),
        'module' => 'field_sql_storage',
        'active' => '1',
        'details' => array(
          'sql' => array(
            'FIELD_LOAD_CURRENT' => array(
              'field_data_field_teams' => array(
                'target_id' => 'field_teams_target_id',
              ),
            ),
            'FIELD_LOAD_REVISION' => array(
              'field_revision_field_teams' => array(
                'target_id' => 'field_teams_target_id',
              ),
            ),
          ),
        ),
      ),
      'foreign keys' => array(
        'node' => array(
          'table' => 'node',
          'columns' => array(
            'target_id' => 'nid',
          ),
        ),
      ),
      'indexes' => array(
        'target_id' => array(
          0 => 'target_id',
        ),
      ),
      'field_permissions' => array(
        'type' => '0',
      ),
      'field_name' => 'field_teams',
      'type' => 'entityreference',
      'module' => 'entityreference',
      'active' => '1',
      'locked' => '0',
      'cardinality' => '-1',
      'deleted' => '0',
      'columns' => array(
        'target_id' => array(
          'description' => 'The id of the target entity.',
          'type' => 'int',
          'unsigned' => TRUE,
          'not null' => TRUE,
        ),
      ),
      'bundles' => array(
        'node' => array(
          0 => 'player',
        ),
      ),
    ),
  ),
  'instances' => array(
    'body' => array(
      0 => array(
        'label' => 'Body',
        'widget' => array(
          'type' => 'text_textarea_with_summary',
          'settings' => array(
            'rows' => 20,
            'summary_rows' => 5,
          ),
          'weight' => '31',
          'module' => 'text',
        ),
        'settings' => array(
          'display_summary' => TRUE,
          'text_processing' => 1,
          'user_register_form' => FALSE,
        ),
        'display' => array(
          'default' => array(
            'label' => 'hidden',
            'type' => 'text_default',
            'settings' => array(),
            'module' => 'text',
            'weight' => 0,
          ),
          'teaser' => array(
            'label' => 'hidden',
            'type' => 'text_summary_or_trimmed',
            'settings' => array(
              'trim_length' => 600,
            ),
            'module' => 'text',
            'weight' => 0,
          ),
        ),
        'required' => FALSE,
        'description' => '',
        'field_name' => 'body',
        'entity_type' => 'node',
        'bundle' => 'player',
        'deleted' => '0',
        'default_value' => NULL,
      ),
    ),
    'field_player_bats' => array(
      0 => array(
        'label' => 'Bats',
        'widget' => array(
          'weight' => '39',
          'type' => 'options_select',
          'module' => 'options',
          'active' => 1,
          'settings' => array(),
        ),
        'settings' => array(
          'user_register_form' => FALSE,
        ),
        'display' => array(
          'default' => array(
            'label' => 'above',
            'type' => 'list_default',
            'settings' => array(),
            'module' => 'list',
            'weight' => 8,
          ),
          'teaser' => array(
            'type' => 'hidden',
            'label' => 'above',
            'settings' => array(),
            'weight' => 0,
          ),
        ),
        'required' => 0,
        'description' => '',
        'default_value' => NULL,
        'field_name' => 'field_player_bats',
        'entity_type' => 'node',
        'bundle' => 'player',
        'deleted' => '0',
      ),
    ),
    'field_player_birthday' => array(
      0 => array(
        'label' => 'Birthday',
        'widget' => array(
          'weight' => '34',
          'type' => 'date_popup',
          'module' => 'date',
          'active' => 1,
          'settings' => array(
            'input_format' => 'm/d/Y - H:i:s',
            'input_format_custom' => '',
            'year_range' => '-3:+3',
            'increment' => '15',
            'label_position' => 'above',
            'text_parts' => array(),
            'no_fieldset' => 0,
          ),
        ),
        'settings' => array(
          'default_value' => 'now',
          'default_value_code' => '',
          'default_value2' => 'same',
          'default_value_code2' => '',
          'user_register_form' => FALSE,
        ),
        'display' => array(
          'default' => array(
            'label' => 'above',
            'type' => 'date_default',
            'settings' => array(
              'format_type' => 'long',
              'multiple_number' => '',
              'multiple_from' => '',
              'multiple_to' => '',
              'fromto' => 'both',
              'show_remaining_days' => FALSE,
            ),
            'module' => 'date',
            'weight' => 3,
          ),
          'teaser' => array(
            'type' => 'hidden',
            'label' => 'above',
            'settings' => array(),
            'weight' => 0,
          ),
        ),
        'required' => 0,
        'description' => '',
        'field_name' => 'field_player_birthday',
        'entity_type' => 'node',
        'bundle' => 'player',
        'deleted' => '0',
      ),
    ),
    'field_player_death' => array(
      0 => array(
        'label' => 'Death',
        'widget' => array(
          'weight' => '35',
          'type' => 'date_popup',
          'module' => 'date',
          'active' => 1,
          'settings' => array(
            'input_format' => 'm/d/Y - H:i:s',
            'input_format_custom' => '',
            'year_range' => '-3:+3',
            'increment' => '15',
            'label_position' => 'above',
            'text_parts' => array(),
            'no_fieldset' => 0,
          ),
        ),
        'settings' => array(
          'default_value' => 'now',
          'default_value_code' => '',
          'default_value2' => 'same',
          'default_value_code2' => '',
          'user_register_form' => FALSE,
        ),
        'display' => array(
          'default' => array(
            'label' => 'above',
            'type' => 'date_default',
            'settings' => array(
              'format_type' => 'long',
              'multiple_number' => '',
              'multiple_from' => '',
              'multiple_to' => '',
              'fromto' => 'both',
              'show_remaining_days' => FALSE,
            ),
            'module' => 'date',
            'weight' => 4,
          ),
          'teaser' => array(
            'type' => 'hidden',
            'label' => 'above',
            'settings' => array(),
            'weight' => 0,
          ),
        ),
        'required' => 0,
        'description' => '',
        'field_name' => 'field_player_death',
        'entity_type' => 'node',
        'bundle' => 'player',
        'deleted' => '0',
      ),
    ),
    'field_player_height' => array(
      0 => array(
        'label' => 'Height',
        'widget' => array(
          'weight' => '37',
          'type' => 'number',
          'module' => 'number',
          'active' => 0,
          'settings' => array(),
        ),
        'settings' => array(
          'min' => '0',
          'max' => '',
          'prefix' => '',
          'suffix' => 'inches',
          'user_register_form' => FALSE,
        ),
        'display' => array(
          'default' => array(
            'label' => 'above',
            'type' => 'number_integer',
            'settings' => array(
              'thousand_separator' => '',
              'decimal_separator' => '.',
              'scale' => 0,
              'prefix_suffix' => TRUE,
            ),
            'module' => 'number',
            'weight' => 6,
          ),
          'teaser' => array(
            'type' => 'hidden',
            'label' => 'above',
            'settings' => array(),
            'weight' => 0,
          ),
        ),
        'required' => 0,
        'description' => '',
        'default_value' => NULL,
        'field_name' => 'field_player_height',
        'entity_type' => 'node',
        'bundle' => 'player',
        'deleted' => '0',
      ),
    ),
    'field_player_id' => array(
      0 => array(
        'label' => 'Player ID',
        'widget' => array(
          'weight' => '33',
          'type' => 'text_textfield',
          'module' => 'text',
          'active' => 1,
          'settings' => array(
            'size' => '60',
            'maxlength_js' => 0,
            'maxlength_js_label' => 'Content limited to @limit characters, remaining: <strong>@remaining</strong>',
          ),
        ),
        'settings' => array(
          'text_processing' => '0',
          'better_formats' => array(
            'allowed_formats_toggle' => 0,
            'allowed_formats' => array(
              'all_html' => 'all_html',
              'filtered_html' => 'filtered_html',
              'full_html' => 'full_html',
              'plain_text' => 'plain_text',
              'plain_text_token_interpolate_only' => 'plain_text_token_interpolate_only',
              'twig_enabled' => 'twig_enabled',
            ),
            'default_order_toggle' => 0,
            'default_order_wrapper' => array(
              'formats' => array(
                'all_html' => array(
                  'weight' => '-10',
                ),
                'filtered_html' => array(
                  'weight' => '-9',
                ),
                'full_html' => array(
                  'weight' => '-8',
                ),
                'plain_text' => array(
                  'weight' => '-7',
                ),
                'plain_text_token_interpolate_only' => array(
                  'weight' => '-6',
                ),
                'twig_enabled' => array(
                  'weight' => '-5',
                ),
              ),
            ),
          ),
          'user_register_form' => FALSE,
        ),
        'display' => array(
          'default' => array(
            'label' => 'above',
            'type' => 'text_default',
            'settings' => array(),
            'module' => 'text',
            'weight' => 2,
          ),
          'teaser' => array(
            'type' => 'hidden',
            'label' => 'above',
            'settings' => array(),
            'weight' => 0,
          ),
        ),
        'required' => 0,
        'description' => '',
        'default_value' => NULL,
        'field_name' => 'field_player_id',
        'entity_type' => 'node',
        'bundle' => 'player',
        'deleted' => '0',
      ),
    ),
    'field_player_nick_name' => array(
      0 => array(
        'label' => 'Nick name',
        'widget' => array(
          'weight' => '32',
          'type' => 'text_textfield',
          'module' => 'text',
          'active' => 1,
          'settings' => array(
            'size' => '60',
            'maxlength_js' => 0,
            'maxlength_js_label' => 'Content limited to @limit characters, remaining: <strong>@remaining</strong>',
          ),
        ),
        'settings' => array(
          'text_processing' => '0',
          'better_formats' => array(
            'allowed_formats_toggle' => 0,
            'allowed_formats' => array(
              'all_html' => 'all_html',
              'filtered_html' => 'filtered_html',
              'full_html' => 'full_html',
              'plain_text' => 'plain_text',
              'plain_text_token_interpolate_only' => 'plain_text_token_interpolate_only',
              'twig_enabled' => 'twig_enabled',
            ),
            'default_order_toggle' => 0,
            'default_order_wrapper' => array(
              'formats' => array(
                'all_html' => array(
                  'weight' => '-10',
                ),
                'filtered_html' => array(
                  'weight' => '-9',
                ),
                'full_html' => array(
                  'weight' => '-8',
                ),
                'plain_text' => array(
                  'weight' => '-7',
                ),
                'plain_text_token_interpolate_only' => array(
                  'weight' => '-6',
                ),
                'twig_enabled' => array(
                  'weight' => '-5',
                ),
              ),
            ),
          ),
          'user_register_form' => FALSE,
        ),
        'display' => array(
          'default' => array(
            'label' => 'above',
            'type' => 'text_default',
            'settings' => array(),
            'module' => 'text',
            'weight' => 1,
          ),
          'teaser' => array(
            'type' => 'hidden',
            'label' => 'above',
            'settings' => array(),
            'weight' => 0,
          ),
        ),
        'required' => 0,
        'description' => '',
        'default_value' => NULL,
        'field_name' => 'field_player_nick_name',
        'entity_type' => 'node',
        'bundle' => 'player',
        'deleted' => '0',
      ),
    ),
    'field_player_notes' => array(
      0 => array(
        'label' => 'Notes',
        'widget' => array(
          'weight' => '40',
          'type' => 'text_textarea',
          'module' => 'text',
          'active' => 1,
          'settings' => array(
            'rows' => '5',
            'maxlength_js' => '',
            'maxlength_js_enforce' => 0,
            'maxlength_js_truncate_html' => 0,
            'maxlength_js_label' => 'Content limited to @limit characters, remaining: <strong>@remaining</strong>',
          ),
        ),
        'settings' => array(
          'text_processing' => '1',
          'better_formats' => array(
            'allowed_formats_toggle' => 1,
            'allowed_formats' => array(
              'filtered_html' => 'filtered_html',
              'all_html' => 0,
              'full_html' => 0,
              'plain_text' => 0,
              'plain_text_token_interpolate_only' => 0,
              'twig_enabled' => 0,
            ),
            'default_order_toggle' => 0,
            'default_order_wrapper' => array(
              'formats' => array(
                'all_html' => array(
                  'weight' => '-10',
                ),
                'filtered_html' => array(
                  'weight' => '-9',
                ),
                'full_html' => array(
                  'weight' => '-8',
                ),
                'plain_text' => array(
                  'weight' => '-7',
                ),
                'plain_text_token_interpolate_only' => array(
                  'weight' => '-6',
                ),
                'twig_enabled' => array(
                  'weight' => '-5',
                ),
              ),
            ),
          ),
          'user_register_form' => FALSE,
        ),
        'display' => array(
          'default' => array(
            'label' => 'above',
            'type' => 'text_default',
            'settings' => array(),
            'module' => 'text',
            'weight' => 9,
          ),
          'teaser' => array(
            'type' => 'hidden',
            'label' => 'above',
            'settings' => array(),
            'weight' => 0,
          ),
        ),
        'required' => 0,
        'description' => '',
        'default_value' => NULL,
        'field_name' => 'field_player_notes',
        'entity_type' => 'node',
        'bundle' => 'player',
        'deleted' => '0',
      ),
    ),
    'field_player_throws' => array(
      0 => array(
        'label' => 'Throws',
        'widget' => array(
          'weight' => '38',
          'type' => 'options_select',
          'module' => 'options',
          'active' => 1,
          'settings' => array(),
        ),
        'settings' => array(
          'user_register_form' => FALSE,
        ),
        'display' => array(
          'default' => array(
            'label' => 'above',
            'type' => 'list_default',
            'settings' => array(),
            'module' => 'list',
            'weight' => 7,
          ),
          'teaser' => array(
            'type' => 'hidden',
            'label' => 'above',
            'settings' => array(),
            'weight' => 0,
          ),
        ),
        'required' => 0,
        'description' => '',
        'default_value' => NULL,
        'field_name' => 'field_player_throws',
        'entity_type' => 'node',
        'bundle' => 'player',
        'deleted' => '0',
      ),
    ),
    'field_player_weight' => array(
      0 => array(
        'label' => 'Weight',
        'widget' => array(
          'weight' => '36',
          'type' => 'number',
          'module' => 'number',
          'active' => 0,
          'settings' => array(),
        ),
        'settings' => array(
          'min' => '0',
          'max' => '',
          'prefix' => '',
          'suffix' => 'lbs',
          'user_register_form' => FALSE,
        ),
        'display' => array(
          'default' => array(
            'label' => 'above',
            'type' => 'number_integer',
            'settings' => array(
              'thousand_separator' => '',
              'decimal_separator' => '.',
              'scale' => 0,
              'prefix_suffix' => TRUE,
            ),
            'module' => 'number',
            'weight' => 5,
          ),
          'teaser' => array(
            'type' => 'hidden',
            'label' => 'above',
            'settings' => array(),
            'weight' => 0,
          ),
        ),
        'required' => 0,
        'description' => '',
        'default_value' => NULL,
        'field_name' => 'field_player_weight',
        'entity_type' => 'node',
        'bundle' => 'player',
        'deleted' => '0',
      ),
    ),
    'field_team_park' => array(
      0 => array(
        'label' => 'Park',
        'widget' => array(
          'weight' => '31',
          'type' => 'text_textfield',
          'module' => 'text',
          'active' => 1,
          'settings' => array(
            'size' => '60',
            'maxlength_js' => 0,
            'maxlength_js_label' => 'Content limited to @limit characters, remaining: <strong>@remaining</strong>',
          ),
        ),
        'settings' => array(
          'text_processing' => '0',
          'better_formats' => array(
            'allowed_formats_toggle' => 0,
            'allowed_formats' => array(
              'all_html' => 'all_html',
              'filtered_html' => 'filtered_html',
              'full_html' => 'full_html',
              'plain_text' => 'plain_text',
              'plain_text_token_interpolate_only' => 'plain_text_token_interpolate_only',
              'twig_enabled' => 'twig_enabled',
            ),
            'default_order_toggle' => 0,
            'default_order_wrapper' => array(
              'formats' => array(
                'all_html' => array(
                  'weight' => '-10',
                ),
                'filtered_html' => array(
                  'weight' => '-9',
                ),
                'full_html' => array(
                  'weight' => '-8',
                ),
                'plain_text' => array(
                  'weight' => '-7',
                ),
                'plain_text_token_interpolate_only' => array(
                  'weight' => '-6',
                ),
                'twig_enabled' => array(
                  'weight' => '-5',
                ),
              ),
            ),
          ),
          'user_register_form' => FALSE,
        ),
        'display' => array(
          'default' => array(
            'label' => 'above',
            'type' => 'text_default',
            'settings' => array(),
            'module' => 'text',
            'weight' => 0,
          ),
          'teaser' => array(
            'type' => 'hidden',
            'label' => 'above',
            'settings' => array(),
            'weight' => 0,
          ),
        ),
        'required' => 0,
        'description' => '',
        'default_value' => NULL,
        'field_name' => 'field_team_park',
        'entity_type' => 'node',
        'bundle' => 'team',
        'deleted' => '0',
      ),
    ),
    'field_teams' => array(
      0 => array(
        'label' => 'Teams',
        'widget' => array(
          'weight' => '41',
          'type' => 'entityreference_autocomplete',
          'module' => 'entityreference',
          'active' => 1,
          'settings' => array(
            'match_operator' => 'CONTAINS',
            'size' => '60',
            'path' => '',
          ),
        ),
        'settings' => array(
          'user_register_form' => FALSE,
        ),
        'display' => array(
          'default' => array(
            'label' => 'above',
            'type' => 'entityreference_label',
            'settings' => array(
              'link' => FALSE,
            ),
            'module' => 'entityreference',
            'weight' => 10,
          ),
          'teaser' => array(
            'type' => 'hidden',
            'label' => 'above',
            'settings' => array(),
            'weight' => 0,
          ),
        ),
        'required' => 0,
        'description' => '',
        'default_value' => NULL,
        'field_name' => 'field_teams',
        'entity_type' => 'node',
        'bundle' => 'player',
        'deleted' => '0',
      ),
    ),
  ),
);
