import os
from pdb4amber import utils
from mock import patch


@patch('parmed.load_file')
def test_get_amber_compatible_resnames(mock_load_file):
    mock_load_file.return_value = {'G3': 'mock'}
    with patch.dict(os.environ, {'AMBERHOME':'/tmp/amber'}):
         assert utils.get_amber_compatible_resnames() == {'G3'}
    with patch.dict(os.environ, {}):
         assert utils.get_amber_compatible_resnames() == set()
