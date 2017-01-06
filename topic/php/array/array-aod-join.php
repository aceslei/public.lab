  <?php
  function array_aod_leftjoin( $aod1, $aod2, $slkey='id', $srkey='', $sgdefault='' ){
    // init func
    $reindexed = Array();
    if((string)$srkey==''){ $srkey = $slkey; }
    // process
    foreach ($aod2 as $tmpval) {
      $reindexed[$tmpval[$srkey]] = $tmpval;
    }
    // process
    $aod2_emptyrow = array_fill_keys(array_keys($aod2[0]), $sgdefault);
    if((string)$slkey==(string)$srkey){
      unset($aod2_emptyrow[$slkey]);
    }
    // process
    foreach ($aod1 as &$tmprow) {
      $tmprow = (@$reindexed[$tmprow[$slkey]])
        ? array_merge($tmprow,$reindexed[$tmprow[$slkey]])
        : array_merge($tmprow,$aod2_emptyrow)
        ;
    }
    // return
    return ( $aod1 );
  }
  //endfunc
  
  $aod3 = array(
            array( "id"=>'001', 'fname'=>'ted',  'lname'=>'miller', 'favetopping'=>'001', ),
            array( "id"=>'002', 'fname'=>'mike', 'lname'=>'miller', 'favetopping'=>'001', ),
            array( "id"=>'003', 'fname'=>'joe',  'lname'=>'simpson','favetopping'=>'002', ),
            array( "id"=>'004', 'fname'=>'tim',  'lname'=>'smith',  'favetopping'=>'003', ),
            array( "id"=>'005', 'fname'=>'tom',  'lname'=>'james',  'favetopping'=>'',    ),
        );

  $aod4 = array(
            array( "id"=>'001', 'topping'=>'beef' ),
            array( "id"=>'002', 'topping'=>'bacon' ),
            array( "id"=>'003', 'topping'=>'chicken' ),
        );
        
  // example usage
  $slkey  =   "favetopping";
  $srkey  =   "id";
  $aod3   =   array_aod_leftjoin( $aod3 , $aod4 , $slkey, $srkey );
  print var_export( $aod3 );
  //;;
?>

RESULT

array (
  0 => 
  array (
    'id' => '001',
    'fname' => 'ted',
    'lname' => 'miller',
    'favetopping' => '001',
    'topping' => 'beef',
  ),
  1 => 
  array (
    'id' => '001',
    'fname' => 'mike',
    'lname' => 'miller',
    'favetopping' => '001',
    'topping' => 'beef',
  ),
  2 => 
  array (
    'id' => '002',
    'fname' => 'joe',
    'lname' => 'simpson',
    'favetopping' => '002',
    'topping' => 'bacon',
  ),
  3 => 
  array (
    'id' => '003',
    'fname' => 'tim',
    'lname' => 'smith',
    'favetopping' => '003',
    'topping' => 'chicken',
  ),
  4 => 
  array (
    'id' => '',
    'fname' => 'tom',
    'lname' => 'james',
    'favetopping' => '',
    'topping' => '',
  ),
)  
