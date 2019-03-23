import os
from pdb4amber import utils
from mock import patch, MagicMock


@patch('parmed.load_file')
def test_get_amber_compatible_resnames(mock_load_file):
    mock_load_file.return_value = {'G3': 'mock'}

    with patch('os.getenv', MagicMock(return_value='/tmp/amber/')), \
            patch('os.path.exists', MagicMock(return_value=True)):
         assert utils.get_amber_compatible_resnames() == {'G3'}

    with patch('os.getenv', MagicMock(return_value=None)):
         assert utils.get_amber_compatible_resnames() == set()
