<?php session_start();?>
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>


<style>
.manish {
    width: 100%;
    border-collapse: collapse;
}

table, td, th {
    border: 1px solid black;
    padding: 5px;
}

th {text-align: left;}
</style>
</head>
<body>
<form action="sort1.php" method="get">
<table border="1" >
<tr>
<td>Sort by Application No</td>
<td><input type="checkbox" name="q0[]" value="Application_No"> </td>
</tr>
<tr>
<td>Sort by Date Of Filing Of Application</td>
<td><input type="checkbox" name="q0[]" value="Date_of_filing_of_Application"></td>
</tr>
<tr>
<td>Sort by Publication Date</td>
<td><input type="checkbox" name="q0[]" value="Publication_Date" ></td>
</tr>
<tr>
<td>Sort by Name of Applicant </td>
<td><input type="checkbox" name="q0[]" value="Name_of_Applicant"></td>
</tr>
<tr>
<td>Sort by Title of Invention </td>
<td><input type="checkbox" name="q0[]" value="Title_of_Invention"></td>
</tr>
<tr>
<td>Sort by Name of Inventor(s) </td>
<td><input type="checkbox" name="q0[]" value="Name_of_Inventor"></td>
</tr>
<tr>
<td>Sort by Abstract </td>
<td><input type="checkbox" name="q0[]" value="Abstract"></td>
</tr>
<tr>
<td>Sort by No.of pages</td>
<td><input type="checkbox" name="q0[]" value="No_of_pages"></td>
</tr>
<tr>
<td>Sort by No. of claims </td>
<td><input type="checkbox" name="q0[]" value="No_of_claims"></td>
</tr>
<tr>
<td>Sort by International classification </td>
<td><input type="checkbox" name="q0[]" value="International_classification"></td>
</tr>
<tr>
<td>Sort by Priority Document No. </td>
<td><input type="checkbox" name="q0[]" value="Priority_Document_No"></td>
</tr>
<tr>
<td>Sort by Priority Date </td>
<td><input type="checkbox" name="q0[]" value="Priority_Date"></td>
</tr>
<tr>
<td>Sort by Name of priority country </td>
<td><input type="checkbox" name="q0[]" value="Name_of_priority_country"></td>
</tr>
<tr>
<td>Sort by International Application No.</td>
<td><input type="checkbox" name="q0[]" value="International_Application_No"></td>
</tr>
<tr>
<td>Sort by International Application Filling Date </td>
<td><input type="checkbox" name="q0[]" value="International_Application_Filing_Date"></td>
</tr>
<tr>
<td>Sort by International Publication No. </td>
<td><input type="checkbox" name="q0[]" value="International_Publication_No"></td>
</tr>
<tr>
<td>Sort by Patent of addition to Application No.</td>
<td><input type="checkbox" name="q0[]" value="Patent_of_addition_to_Application_No"></td>
</tr>
<tr>
<td>Sort by Patent of addition to Application No. Filling Date </td>
<td><input type="checkbox" name="q0[]" value="Patent_of_addition_to_Application_No_Filing_Date"></td>
</tr>
<tr>
<td>Sort by Divisional to Application No. </td>
<td><input type="checkbox" name="q0[]" value="Divisional_to_Application_No"></td>
</tr>
<tr>
<td>Sort by Divisional to Application No. Filling Date </td>
<td><input type="checkbox" name="q0[]" value="Divisional_to_Application_No_Filing_Date"></td>
</tr>
<tr>

</tr>
</table>
<input type="submit" >
</form>

<h6>SEARCH BY </h6>
<form action="sort1.php">
  <select name="search_by">
    <option value="Application_No">Application No.</option>
    <option value="Date_of_filing_of_Application">Date Of Filing Of Application</option>
    <option value="Publication_Date">Publication Date</option>
    <option value="Name_of_Applicant">Name of Applicant</option>
	<option value="Title_of_Invention">Title of Invention</option>
	<option value="Name_of_Inventor">Name of Inventor(s)</option>
	<option value="Abstract">Abstract</option>
	<option value="No_of_pages">No.of pages</option>
	<option value="No_of_claims">No.of claims</option>
	<option value="International_classification">International_classification</option>
	<option value="Priority_Document_No">Priority Document No.</option>
	<option value="Priority_Date">Priority Date</option>
	<option value="Name_of_priority_country">Name of priority country</option>
	<option value="International_Application_No">International Application No.</option>
	<option value="International_Application_Filing_Date">International_Application_Filing_Date</option>
	<option value="International_Publication_No">International Publication No.</option>
	<option value="Patent_of_addition_to_Application_No">Patent of addition to Application No.</option>
	<option value="Patent_of_addition_to_Application_No_Filing_Date">Patent of addition to Application No. Filling Date</option>
	<option value="Divisional_to_Application_No">Divisional to Application No.</option>
	<option value="Divisional_to_Application_No_Filing_Date">Divisional to Application No. Filling Date</option>
	Select : <input type="text" name="name"><br>
  </select>
  <br><br>
  <input type="submit">
</form>

<?php

if(isset($_GET["name"])and isset($_GET["search_by"]))
{echo $_GET["name"];
echo $_GET["search_by"];
}
$con = mysqli_connect('localhost','root','','patents');
if (!$con) {
    die('Could not connect: ' . mysqli_error($con));
}

if(isset($_GET["q0"]))
{

	$value[]=$_GET['q0'];
	if(!empty($value))
	{
		$q="";
		
		for($i=0 ; $i<count($value);$i++)
		{
			
			for($j=0 ; $j<count($value[$i]);$j++)
			{
			  $q .=$value[$i][$j];
			 $q .=",";
			}
			
			
		}
	
     
	 $q= substr($q,0,(strlen($q)-1));
	 echo $q."<br>";
//$sql="SELECT * FROM patent_tables ORDER BY 'Application_No'";
$sql1 = "Select * from patent_tables ORDER BY $q";
$SESSION['manish1']=$q;
/*$sql1+="'Application_No',";
$sql1+="'Date_of_filing_of_Application',";
$sql1+="'Publication_Date',";
$sql1+="'Name_of_Applicant',";
$sql1+="'Title_of_Invention',";
$sql1+="'Name_of_Inventor',";
$sql1+="'Abstract',";
$sql1+="'No_of_pages',";
$sql1+="'No_of_claims',";
$sql1+="'International_classification',";
$sql1+="'Priority_Document_No',";
$sql1+="'Priority_Date',";
$sql1+="'Name_of_priority_country',";
$sql1+="'International_Application_No',";
$sql1+="'International_Application_Filing_Date',";
$sql1+="'International_Publication_No',";
$sql1+="'Patent_of_addition_to_Application_No',";
$sql1+="'Patent_of_addition_to_Application_No_Filing_Date',";
$sql1+="'Divisional_to_Application_No',";
$sql1+="'Divisional_to_Application_No_Filing_Date',";
substr($sql1,0,(strlen($sql1)-2));*/

$result = mysqli_query($con,$sql1);
if($result==true)
echo "
<table class='manish'>
<tr>
<th>Application No.</th>
<th>Date of filling of Application</th>
<th>Publication Date</th>
<th>Name of Applicant</th>
<th>Title of Invention</th>
<th>Name of Inventor(s)</th>
<th>Abstract</th>
<th>No. of pages</th>
<th>No. of claims</th>
<th>International classification</th>
<th>Priority Document No.</th>
<th>Priority Date</th>
<th>Name of priority country</th>
<th>International Application No.</th>
<th>International Application Filling Date</th>
<th>International Publication No.</th>
<th>Patent of addition to Application No.</th>
<th>Patent of addition to Application No. Filling Date</th>
<th>Divisional to Application No.</th>
<th>Divisional to Application No. Filling Date</th>
</tr>";
if($result==true){
while($row = mysqli_fetch_array($result)) {
    echo "<tr>";
    echo "<td>" . $row['Application_No'] . "</td>";
    echo "<td>" . $row['Date_of_filing_of_Application'] . "</td>";
    echo "<td>" . $row['Publication_Date'] . "</td>";
    echo "<td>" . $row['Name_of_Applicant'] . "</td>";
	echo "<td>" . $row['Title_of_Invention'] ."</td>";
    echo "<td>" . $row['Name_of_Inventor'] . "</td>";
	echo "<td>" . $row['Abstract'] ."</td>";
	echo "<td>" . $row['No_of_pages'] ."</td>";
	echo "<td>" . $row['No_of_claims'] ."</td>";
	echo "<td>" . $row['International_classification'] ."</td>";
	echo "<td>" . $row['Priority_Document_No'] ."</td>";
	echo "<td>" . $row['Priority_Date'] ."</td>";
	echo "<td>" . $row['Name_of_priority_country'] ."</td>";
	echo "<td>" . $row['International_Application_No'] ."</td>";
	echo "<td>" . $row['International_Application_Filing_Date'] ."</td>";
	echo "<td>" . $row['International_Publication_No'] ."</td>";
	echo "<td>" . $row['Patent_of_addition_to_Application_No'] ."</td>";
	echo "<td>" . $row['Patent_of_addition_to_Application_No_Filing_Date'] ."</td>";
	echo "<td>" . $row['Divisional_to_Application_No'] ."</td>";
	echo "<td>" . $row['Divisional_to_Application_No_Filing_Date'] ."</td>";
	
    echo "</tr>";
}
}
else
	echo "TABLE EMPTY";
echo "</table>";
mysqli_close($con);
}
}
if(isset($_GET["search_by"]) and isset($_GET["name"]))
{
$searchby = $_GET["search_by"];
$search = $_GET["name"];
//$sql="SELECT * FROM patent_tables ORDER BY 'Application_No'";
$sql1 = "Select * from patent_tables where ".$searchby." like '%".$search."%'";
$_SESSION['manish2']=$searchby;
$_SESSION['name']=$search;
echo $_SESSION['name'];
/*$sql1+="'Application_No',";
$sql1+="'Date_of_filing_of_Application',";
$sql1+="'Publication_Date',";
$sql1+="'Name_of_Applicant',";
$sql1+="'Title_of_Invention',";
$sql1+="'Name_of_Inventor',";
$sql1+="'Abstract',";
$sql1+="'No_of_pages',";
$sql1+="'No_of_claims',";
$sql1+="'International_classification',";
$sql1+="'Priority_Document_No',";
$sql1+="'Priority_Date',";
$sql1+="'Name_of_priority_country',";
$sql1+="'International_Application_No',";
$sql1+="'International_Application_Filing_Date',";
$sql1+="'International_Publication_No',";
$sql1+="'Patent_of_addition_to_Application_No',";
$sql1+="'Patent_of_addition_to_Application_No_Filing_Date',";
$sql1+="'Divisional_to_Application_No',";
$sql1+="'Divisional_to_Application_No_Filing_Date',";
substr($sql1,0,(strlen($sql1)-2));*/

$result = mysqli_query($con,$sql1);
if($result==true)
echo "<table class='nitish'><tr>
<th>Application No.</th>
<th>Date of filling of Application</th>
<th>Publication Date</th>
<th>Name of Applicant</th>
<th>Title of Invention</th>
<th>Name of Inventor(s)</th>
<th>Abstract</th>
<th>No. of pages</th>
<th>No. of claims</th>
<th>International classification</th>
<th>Priority Document No.</th>
<th>Priority Date</th>
<th>Name of priority country</th>
<th>International Application No.</th>
<th>International Application Filling Date</th>
<th>International Publication No.</th>
<th>Patent of addition to Application No.</th>
<th>Patent of addition to Application No. Filling Date</th>
<th>Divisional to Application No.</th>
<th>Divisional to Application No. Filling Date</th>
</tr>";
if($result==true){
while($row = mysqli_fetch_array($result)) {
    echo "<tr>";
    echo "<td>" . $row['Application_No'] . "</td>";
    echo "<td>" . $row['Date_of_filing_of_Application'] . "</td>";
    echo "<td>" . $row['Publication_Date'] . "</td>";
    echo "<td>" . $row['Name_of_Applicant'] . "</td>";
	echo "<td>" . $row['Title_of_Invention'] ."</td>";
    echo "<td>" . $row['Name_of_Inventor'] . "</td>";
	echo "<td>" . $row['Abstract'] ."</td>";
	echo "<td>" . $row['No_of_pages'] ."</td>";
	echo "<td>" . $row['No_of_claims'] ."</td>";
	echo "<td>" . $row['International_classification'] ."</td>";
	echo "<td>" . $row['Priority_Document_No'] ."</td>";
	echo "<td>" . $row['Priority_Date'] ."</td>";
	echo "<td>" . $row['Name_of_priority_country'] ."</td>";
	echo "<td>" . $row['International_Application_No'] ."</td>";
	echo "<td>" . $row['International_Application_Filing_Date'] ."</td>";
	echo "<td>" . $row['International_Publication_No'] ."</td>";
	echo "<td>" . $row['Patent_of_addition_to_Application_No'] ."</td>";
	echo "<td>" . $row['Patent_of_addition_to_Application_No_Filing_Date'] ."</td>";
	echo "<td>" . $row['Divisional_to_Application_No'] ."</td>";
	echo "<td>" . $row['Divisional_to_Application_No_Filing_Date'] ."</td>";
	
    echo "</tr>";
}
}
else
	echo "TABLE EMPTY";
echo "</table>";

////////////////////////
echo '
<div class="container">
 <br />
<br />
<br />
<div class="table-responsive">
<h2align="center">Export Mysql data to Excel in php</h2><br />
<div class="table-responsive">
    <h2 align="center">Export Mysql data to Excel in Php</h2><br/>
    <div id="LIVE_DATA"></div>
    <form action="test.php" method="post">
          <input type="submit" name="export_excel" class="btn btn-success" value="Export to excel">
    </form>';

$con= new mysqli('localhost','root','','patents');

if(isset($_POST['export_excel']))
{
	
//$sql="SELECT * FROM  patent_tables order by $sql1 ";
/*if(isset($SESSION['manish1']))
{
if(!empty($SESSION['manish1']))
{
	$sql3= 'Select * from patent_tables ORDER BY $SESSION["manish1"]';
	$SESSION['manish1']="";
	
}
}*/
if(isset($_SESSION['manish2']))
{
if(!empty($_SESSION['manish2']))
{
    echo $_SESSION['manish2'] ." hii " .$_SESSION['name'];
	
	$sql3 = "Select * from patent_tables where ".$_SESSION['manish2']." like '%".$_SESSION['name']."%'";						
	
}

$result=$con->query($sql3);
$output ='';
$output .='<table class="table" bordered="1">
<tr>
<th>Application No.</th>
<th>Date of filling of Application</th>
<th>Publication Date</th>
<th>Name of Applicant</th>
<th>Title of Invention</th>
<th>Name of Inventor(s)</th>
<th>Abstract</th>
<th>No. of pages</th>
<th>No. of claims</th>
<th>International classification</th>
<th>Priority Document No.</th>
<th>Priority Date</th>
<th>Name of priority country</th>
<th>International Application No.</th>
<th>International Application Filling Date</th>
<th>International Publication No.</th>
<th>Patent of addition to Application No.</th>
<th>Patent of addition to Application No. Filling Date</th>
<th>Divisional to Application No.</th>
<th>Divisional to Application No. Filling Date</th>
</tr>';

if ($result->num_rows > 0) {
  while($row=$result->fetch_assoc())
{
  $output .='
            <tr>
     <td>' . $row['Application_No'] .'</td>
     <td>' . $row['Date_of_filing_of_Application'] . '</td>
     <td>' . $row['Publication_Date'] . '</td>
     <td>' . $row['Name_of_Applicant'] . '</td>
	 <td>' . $row['Title_of_Invention'] .'</td>
     <td>' . $row['Name_of_Inventor'] . '</td>
	 <td>' . $row['Abstract'] .'</td>
	 <td>' . $row['No_of_pages'] .'</td>
	 <td>' . $row['No_of_claims'] .'</td>
	 <td>' . $row['International_classification'] .'</td>
	 <td>' . $row['Priority_Document_No'] .'</td>
	 <td>' . $row['Priority_Date'] .'</td>
	 <td>' . $row['Name_of_priority_country'] .'</td>
	 <td>' . $row['International_Application_No'] .'</td>
	 <td>' . $row['International_Application_Filing_Date'] .'</td>
	 <td>' . $row['International_Publication_No'] .'</td>
	 <td>' . $row['Patent_of_addition_to_Application_No'] .'</td>
	 <td>' . $row['Patent_of_addition_to_Application_No_Filing_Date'] .'</td>
	 <td>' . $row['Divisional_to_Application_No'] .'</td>
	 <td>' . $row['Divisional_to_Application_No_Filing_Date'] .'</td>
	
     </tr>';
}
}
   $output .='</table>';
   header("Content-Type:application/xls");
   header("content-Disposition: attachment;filename=download.xls");
   echo $output;
}
}


}
mysqli_close($con);
?>
</body>
</html>