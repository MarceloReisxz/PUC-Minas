SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: codigo-usuario; Type: SEQUENCE; Schema: public; Owner:
--

CREATE SEQUENCE public."codigo-usuario"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 1000000
    CACHE 1;


ALTER TABLE public."codigo-usuario" OWNER TO x;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: usuario; Type: TABLE; Schema: public; Owner:
--

CREATE TABLE public.usuario (
    codigo integer DEFAULT nextval('public."codigo-usuario"'::regclass) NOT NULL,
    login text UNIQUE,
    email text UNIQUE
);


ALTER TABLE public.usuario OWNER TO x;

--
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner:
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (codigo);


--
-- PostgreSQL database dump complete
--   

