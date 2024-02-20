{ pkgs ? import <nixpkgs> {} }:

let
  python = pkgs.python311;
in pkgs.mkShell {
    name = "python-env";
    buildInputs = with pkgs.python311Packages; [
      python-dotenv
      requests
      spotipy
      venvShellHook
    ];
    src = null;
    shellHook = ''
      virtualenv --no-setuptools venv
      export PATH=$PWD/venv/bin:$PATH
      export PYTHONPATH=venv/lib/python3.11/site-packages/:$PYTHONPATH
    '';
    postShellHook = ''
      unset SOURCE_DATE_EPOCH
      PYTHONPATH=$PWD/venv/${python.sitePackages}:$PYTHONPATH
    '';
}
