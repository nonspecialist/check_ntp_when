% check\_ntp\_when(1) | Version 0.1
% Colin Panisset
% May 21, 2013

# NAME

`check_ntp_when` - check how recently an NTP client polled its server(s)

# SYNOPSIS

`check_ntp_when -H <host> [-w <warn range>] [-c <critical range>] [-n]`

# DESCRIPTION

In certain cases, an NTP client can "forget" to poll its chosen servers,
and will begin to drift from the correct time. This is most often
observed with certain ESXi versions, where the host can forget to poll
its defined NTP servers for hundreds of days.

check\_ntp\_when queries the named NTP client to determine how recently
it contact its NTP server(s). It makes use of the (installed) `ntpq`
client and parses the output.

Unlike the existing nagios plugins `check_ntp_peer` and `check_ntp_time`,
this check does not attempt to validate how "in sync" a given host is
with its NTP servers.

**-H host**

> Specify the host to query. The target system _must_ have
> had NTP configured to permit queries from the monitoring host, otherwise
> the query will time out (and fail)

**-w warning range** 

> define the permissible lag in seconds between the
> poll frequency and the last time that the NTP client contacted its server
> before issuing a WARNING.  The default value is 64 seconds. For
> example, if a client host is currently polling with a frequency of 256
> seconds, then `check_ntp_when` would enter WARNING state once the
> client hadn't contacted the host for 320 seconds.

**-c critical range** 

> define the permissible lag in seconds between the
> poll frequency and the last time that the NTP client contacted it
> server before issuing a CRITICAL. The default value is 256 seconds. For
> example, a host polling every 64 seconds that hadn't contacted its
> server for 320 seconds would enter a CRITICAL state.

**-n** 

> do not attempt to do DNS reverse-lookups on NTP server
> addresses.

# EXAMPLES

Query the local system and emit a WARNING if the NTP client hasn't
contacted the server within 32 seconds after it should have, and go
CRITICAL if it hasn't contacted the server 64 seconds after it should
have.

    $ check_ntp_when -H localhost -w 32 -c 64

# AUTHOR

`check_ntp_when` was written by Colin Panisset <nonspecialist@clabber.com>

# BUGS

Please report bugs via https://github.com/nonspecialist/check_ntp_when

# COPYRIGHT

Copyright (c) 2013 Colin Panisset. `check_ntp_when` is distributed 
under the Gnu GPL v3+ or later http://gnu.org/licenses/gpl.html
There is NO WARRANTY, to the extent permitted by law.
