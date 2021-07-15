export ZSH="/Users/kevin/.oh-my-zsh"
export ZSHCONFIG="/Users/kevin/.zsh"

ZSH_THEME="robbyrussell"

plugins=(git docker docker-compose)

source $ZSH/oh-my-zsh.sh

# CUSTOM
source $ZSHCONFIG/aliases.zsh
source $ZSHCONFIG/command-line-tools.zsh
