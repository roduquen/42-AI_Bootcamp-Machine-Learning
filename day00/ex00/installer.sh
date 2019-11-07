# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    installer.sh                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roduquen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 09:54:55 by roduquen          #+#    #+#              #
#    Updated: 2019/11/04 10:22:33 by roduquen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

TESTPYTHON=`python -V`
NICEVERSION="Python 3.7.4"
ACCEPT="y"
if [ "$TESTPYTHON" = "$NICEVERSION" ]
then
	echo Python is already installed, do you want to reinstall it ?
	printf "[y|n] > "
	read ACCEPT
	if [ "$ACCEPT" = "y" ]
	then
		rm -rf /sgoinfre/goinfre/Perso/roduquen/bootcamp/miniconda/
		echo Python has been removed.
		curl https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh > install.sh
		sh install.sh
		echo Python has been installed.
		rm -rf install.sh
	fi
else
	curl https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh > install.sh
	sh install.sh
	echo Python has been installed.
	rm -rf install.sh
fi
export PATH=/sgoinfre/goinfre/Perso/roduquen/bootcamp/miniconda/bin:$PATH
