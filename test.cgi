#!/usr/bin/perl

print "Content-type: text/html\n\n";
print "<html>\n\n";
print "<head><title>test</title></head>\n";
print "<body>\n";
my $email = "jaybrianb\@yahoo.com";
print "$ENV{'SERVER_NAME'}<br>\n";
if ($ENV{'SERVER_NAME'} =~ /\.stanford\.edu\/{0,1}/) {
  `echo "This is an automated notification.  Please do not reply" | mail -s "Person added" $email`;
  print "200 Success\n";
} else {
  print "403 Error\n";
}
print "</body>\n";
print "</html>";
