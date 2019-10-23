from os import system as sys
import time

defaults = ['develop', 'test', 'review']

class SVC:
    def init(self):
        sys('git config credential.helper store')

        self.user = edmondenovate
        self.password = sylar963

        self.Access = {
            'user':self.user,
            'password':self.password
        }

    def create_and_branch(self, branch_name):
        success = ' Create branch {}'.format(branch_name)
        error = 'somthing went wrong'
        try:
            sys('git checkout -b {}'.format(branch_name))
            sys('git push origin {}'.format(branch_name))

            return (success)
        except Exception as error:
            return (error)

    def project_init(self):
        
        for branch in defaults:
            try:
                sys('git checkout -b {}'.format(branch))
                sys('git push origin {}'.format(branch))

                print('created branch {}'.format(branch))
            except Exception as error:
                print (error)
                return (error)

        return ('Projected Initiation complete')


    def clean(self):
        try:
            sys('git checkout master')
            sys('git branch | grep -v "master" | xargs git branch -D ')
            return ('Cleaned all local branches')

        except Exception as error:
            return (error)
            
